"""scratchctl — console for the scorer (SPEC §8.6).

  python3 -m sp1v3.scratchctl status                 # one command
  python3 -m sp1v3.scratchctl                        # interactive prompt
  python3 -m sp1v3.scratchctl --host 192.168.1.50    # from the PC (scorer started with --listen 0.0.0.0)
  python3 -m sp1v3.scratchctl --script session.txt   # run a file of commands (blind A/B scripts)

Nothing sent from here can energise the actuator rail: the rail exists only while the
hold-to-run lever is held and every hardware element of the loop is closed.
"""
from __future__ import annotations

import argparse
import socket
import sys


class Console:
    def __init__(self, host="127.0.0.1", port=7700, timeout=10.0):
        self.sock = socket.create_connection((host, port), timeout=timeout)
        self.f = self.sock.makefile("rwb")

    def cmd(self, line: str) -> str:
        self.f.write((line.strip() + "\n").encode())
        self.f.flush()
        out = []
        for raw in self.f:
            s = raw.decode(errors="replace").rstrip("\n")
            if s == ".":
                break
            out.append(s)
        return "\n".join(out)

    def close(self):
        try:
            self.sock.close()
        except OSError:
            pass


def main(argv=None):
    ap = argparse.ArgumentParser(description="SP1 v3 console")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=7700)
    ap.add_argument("--script", help="file with one command per line ('#' comments)")
    ap.add_argument("command", nargs="*")
    a = ap.parse_args(argv)
    try:
        c = Console(a.host, a.port)
    except OSError as ex:
        print(f"cannot reach scorer at {a.host}:{a.port}: {ex}\n"
              "is it running?  (systemctl status sp1-scorer)", file=sys.stderr)
        return 2
    try:
        if a.command:
            print(c.cmd(" ".join(a.command)))
        elif a.script:
            for line in open(a.script):
                line = line.split("#", 1)[0].strip()
                if line:
                    print(f"> {line}\n{c.cmd(line)}")
        else:
            print("SP1 v3 console. 'help' for commands, 'quit' to leave.")
            while True:
                try:
                    line = input("sp1> ")
                except (EOFError, KeyboardInterrupt):
                    break
                if line.strip() in ("quit", "exit"):
                    break
                if line.strip():
                    print(c.cmd(line))
    finally:
        c.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
