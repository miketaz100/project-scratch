# S0 build and test guide: S0a "Does it feel good?" and S0b "Will the machine work?"

**Project SCRATCH · SP1 v3 · 14-build/S0 · S0 kit engineer · 2026-10-02**

**Written for** Michael as builder, and for one helper on the day of the scalp session.

**Binding documents:**
- SYSTEM-SPEC-v3 §10 Stage S0, §4.1–4.5 and §8.2;
- safety ruling C1–C8;
- leap4-A §4(e) (dish bench), leap4-D (e) (ink rig), leap4-E (e) (Klipper and hinge tests);
- 13-outsourcing §5.

**Files in this package:**
- `cart-S0a.md`, `cart-S0b.md`;
- `cad/` (STLs, OpenSCAD, README with print settings);
- `klipper/` (printer.cfg, path generator, timing script);
- `CONFLICTS.md`. Read **#1 before the scalp session**.

---

## 0. What S0 is, in one page

**S0a: does it feel good?** About $100–125 plus printing, one weekend, about 8–10 hours.
- **The dish bench** answers the deciding question. Three spring-loaded drafted-cone nails ride a printed dish. The dish lets them down in the middle of each stroke and lifts them clear near the ends. You drive it by hand through printed templates:
  - first on a 7 in ball, to check the geometry;
  - then a helper holds it on your crown, for the sensation.
- **The hand rake.** The same three nails, stroked by the helper's hand on moving skids. It is the comparison for one known spec issue.
- **The helmet fit test.** A $17 bike helmet, two of the real hinges, a stick bail and a bag of coins. It tests whether hand-moving the halo between bouts is acceptable.

**S0b: will the machine work?** About $436, one or two weekends, about 10–14 hours. **Buy it only after S0a is GO.**
- **The Klipper streaming test.** The real Stage A controller (BTT Manta M8P V2.0 + CB1) streams a precessing line as three cable lengths. An LED stands in for a valve, and a logic analyser times it.
- **The tendon ink rig.** Three motors with drums pull three cables through 1.6 m housings to a pen on marbles. The pen draws the path on paper, so you can measure how well the cables copy it.

**Before you start S0a, read `CONFLICTS.md` #1.** Built exactly as the spec freezes it, the dish moves the nails on the scalp only about 10 mm per stroke, not the 17–24 mm the spec expects. The nails land at about 50°, not ≤ 35°.
- The bench is built to the spec on purpose, so that it measures this.
- The scalp session therefore compares the dish rake with a 25 mm hand rake that uses the same nails.
- Your ratings decide whether the problem is "the dish geometry" (fixable on paper) or "the nails themselves" (back to tips and force).

**Order of work:**
1. §2: buy (cart-S0a) and print (cad/README).
2. §3: tape fit, 20 min.
3. §4: helmet test, 1.5 h plus 20 min of TV.
4. §5: build the bench, about 4 h.
5. §6: bench tests on the ball, about 2 h.
6. §7: scalp session, 45 min including setup.
7. §8: GO / NO-GO.
8. If GO: cart-S0b, then §9 Klipper (about 5 h) and §10 ink rig (about 6 h), then §11.

---

## 1. Safety: read this before touching anything

These rules apply at bench stage too. Print this page and keep it on the bench.

**Eyes**
- **Safety glasses** for anyone at the bench while springs, magnets, cut wire or a powered rig are in use.
- **Glasses for both people** during the scalp session. This is the same rule as the spec's session entry (B6).

**Force limits (scalp session)**
- **Per nail:** about 0.12–0.35 N (12–35 g on the scale) in the working range, measured in step D10. **Never set above 0.45 N (45 g).**
- **On the deck:** the helper only steadies it. The bench rests on your head by its own weight, about 150 g. **The helper never presses down.** If a nail bottoms out it becomes a rigid stick, and pressing would then load one Ø 2 mm tip.
- **Push the C-arm only at its low round grip,** never at the top bar. Pushing high tips the block in its dish.

**Breakaway (safety ruling C1)**
- Each nail is held to its plunger by a small magnet that lets go at 12–25 g of pull.
- The **penny test** (step D9) must pass on the day of the session.
- **Count the nails before and after every bout: 3 in, 3 out.** If a nail is missing, it is in your hair. Stop, find it, and inspect the hair at that spot.

**Stop immediately if any of these happen. Lift the bench straight up and off; do not drag it sideways.**
- You say "stop", or raise a hand.
- Any pain, sting, sharp point, heat, tug, pull or catch.
- A nail is missing, or a part feels loose.
- The bench tips or rocks on your head.
- The helper is unsure about anything.

**When not to use it on the scalp**
- Not on broken, sunburnt, irritated or recently treated scalp, or on any scalp condition.
- Not within 30 mm of the hairline, ears or eyes. **This session is crown only.**
- Hair must be clean, dry, combed and free of product. Long hair is tied away from the C-arm.

**Session length:** at most 20 minutes of total contact time per day. Check the scalp afterwards: any redness should be gone within 10 minutes.

**Magnets**
- 3 mm neodymium discs are a **swallowing hazard**. Two swallowed magnets can pinch the gut.
- Keep the bag sealed and away from children and pets. Count them out and back.

**Superglue:** gloves, ventilation, and keep a damp cloth handy. If it bonds skin, peel it apart slowly with warm soapy water.

**S0b electrical**
- Use only the certified 24 V adapter. Nothing in the rig touches mains.
- Plug and unplug driver modules, motors and the CB1 **only with power off**.
- **A stepper driver inserted backwards dies instantly.** Match the EN pin to the board silkscreen.

**S0b mechanical**
- A running drum winds cable with up to about 9 N. Keep fingers, hair and sleeves off the drums.
- Lifting the cable off a running drum can whip.
- Power off before touching the rig.

---

## 2. Tools, workspace, buying and printing

**Tools you need for S0a:**
- a small Phillips and flat screwdriver;
- the 1.5 / 2 / 2.5 mm hex keys that come with the M3 kit;
- side cutters (wire snips);
- scissors;
- a steel ruler with mm marks;
- 400-grit sandpaper;
- a fine-point permanent marker and a washable marker;
- a pin or toothpick;
- a phone with 240 frames-per-second slow motion. iPhone: Camera > Slo-Mo.

**Strongly recommended:** a digital caliper. Harbor Freight 63586, **$11.99** [cited]. You will use it in S0b and Stage A anyway.

**Workspace**
- A table with good light and a towel spread out, so small parts do not roll away.
- A muffin tin or egg carton to sort screws and parts.

**Buying:** `cart-S0a.md`. One Walmart order, one Amazon order, one Bossard order for the 2 hinges, and Home Depot / Michaels pickups.

**Printing:** `cad/README.md`.
- **If you own an FDM printer,** print everything there in PLA or PETG. Print the 11 nails too, for the first evening.
- **Order resin nails before the scalp session.** Their tips come out much cleaner.
- **If you have no printer,** upload the STL list in the README to JLC3DP, or see cart-S0a §C.

**The S0a printed parts:**

| Part | What it is |
|---|---|
| D01 | deck |
| D02 | block |
| D03 | nose plate |
| D04 | plungers ×4 |
| D05 | seat discs ×4 |
| D06 / D07 / D16 | nails |
| D08 | C-arm |
| D09–D11 | templates |
| D12 | skid ring |
| D13 | ball cradle |
| D14 | side mock (optional) |
| D15 | lift gauge |
| H01 | hinge pads ×2 |

**How the nails are named.** The rings on the top of each nail tell you its length:
- **N20**, 1 ring: lets the nail drop 2.0 mm below the surface of a true 170 mm (R 85) ball, when free of it.
- **N30**, 2 rings: 3.0 mm.
- **N35**, 3 rings: 3.5 mm.

That drop is the **reserve**: how far the nail would go further if the scalp were not there. On a 7 in (178 mm) ball, N30 behaves like N20 on a true R 85 ball.

---

## 3. S0a-1: Tape fit of your head (spec V1), 20 minutes

**What it proves.** Nothing pass/fail. It gives your head numbers for the halo work package, replacing the 50th-percentile design head, and it records your hair.

**Parts:** soft tape measure, a helper, a mirror, this sheet.

**Steps**
1. **Head circumference.** Tape level, just above the eyebrows and over the widest part of the back of the head. Pull snug, not tight. Read in mm.
2. **Ear-to-ear over the top.** From the top of one ear opening, where the ear meets the head, straight over the crown to the same point on the other ear.
3. **Front-to-back over the top.** From the bridge of the nose, between the eyebrows, over the crown to the bony bump at the back of the skull (the inion).
4. **Hairline to crown.** From the front hairline at the centre, back to the point where hair swirls (the whorl).
5. **Hair length** at the crown. Pull a few hairs straight up and measure root to tip.
6. **Hair pile** at the crown: how thick the hair layer is when lying naturally. Lay the ruler flat on the hair and push a toothpick down through the hair until it touches the scalp; the depth is the pile.
7. **Whorl direction.** Look down at the crown in a mirror and note which way the hair lies there: front to back, clockwise, or anticlockwise. This sets the "with the grain" direction of the D-path in §7.

**Results sheet S0a-1**

| Measurement | Value |
|---|---|
| Head circumference (mm) | |
| Ear to ear over the top (mm) | |
| Nose bridge to inion over the top (mm) | |
| Front hairline to whorl (mm) | |
| Hair length at crown (mm) | |
| Hair pile at crown (mm) | |
| Hair lies toward (front / back / left / right / swirl CW / CCW) | |
| Date, helper | |

---

## 4. S0a-2: Helmet, hinge and coin-bag test (leap4-E E4), 1.5 h build + 20 min of TV

**What it proves.** That a halo moved **by hand** between bouts, on two bought friction hinges, stays where you put it and does not annoy you. This is spec decision C23. If it fails, powered travel comes back (SP1.5).

**Parts:**
- the bike helmet with a rear dial;
- 2 × Southco E6-10-101-20 hinges, each with 4 nuts;
- 2 × H01 hinge pads (or two small aluminum angle brackets);
- the 1/2 in × 1/16 in × 36 in aluminum bar;
- 6 zip ties and double-sided foam tape;
- a zip bag with about 340 g of coins: 60 quarters, or 136 pennies. Weigh it on the scale in steps, 100 g at a time.

**How the hinge works.** Each E6 hinge has two leaves on a pin, with a set torque of 0.25 N·m. Each leaf carries 2 threaded studs, 15.1 mm apart. Nuts are supplied.

**Build**
1. **Fit the helmet first.** Put it on, turn the rear dial until it is snug, and look straight ahead in a mirror. The front edge sits about two fingers above the eyebrows.
2. **Find the hub points.** With the helmet on, ask the helper to mark a dot on the helmet shell on each side, 45 mm straight above your ear opening. If there is a vent near the dot, use it for the zip ties.
3. **Mount a hinge on each pad.** The pad (H01) is an L-bracket: a **base** that sits flat on the side of the helmet, and a **flange** that sticks straight out sideways at its top edge.
   - Lay one hinge leaf on top of the flange and push its two studs down through the flange holes. Put a nut on each stud from underneath (in the hex pockets) and tighten with pliers.
   - The hinge **pin must point straight out from your head, ear to ear.** That is the spec's α axis: the bail then swings forward and back over the top of your head, like a car's sun visor.
   - If the pin points front-to-back instead, the leaf is on the wrong way round: turn it over.
   - No printer: a 1 × 1 in aluminum angle bracket drilled 7/32 in, with holes 15.1 mm apart, does the same job.
4. **Fix the pads.** Stick foam tape on the back of each base. Press it onto the dot, with the hinge pin's centre level with the dot. Pass 2 zip ties through the base slots and the nearest vents and pull them tight. Snip the tails.
5. **Make the bail.**
   1. Take the aluminum bar off the helmet. Bend it by hand over a round object of about 150 mm radius: a large paint can or a bucket. You want a hoop that goes from one hinge, up over the helmet, to the other, standing about 30–40 mm clear of the shell all the way over.
   2. Mark where each end meets its free hinge leaf. Cut the excess with a hacksaw or snips.
   3. Drill two 7/32 in (5.5 mm) holes in each end, 15.1 mm apart (use calipers), so the free leaf's studs pass through. The last 30 mm of each end lies flat on its free leaf, running outward along the pin. Bend the bar 90° up just past the leaf.
   4. Fit with nuts.
   5. Check: the bail now swings freely forward and back, and stays wherever you leave it.
6. **Coin bag.** Tape the coin bag to the top of the bail, at the point above the crown. With the bail at about 105 mm from the hinge axis, this gives about 0.35 N·m, the worst case in leap4-E.

**Run**
1. **Hold test.** Wear it. Set the bail straight up (α 0°, over the top). Watch 20 min of TV and do not touch it. Every 5 min the helper checks that the bail has not crept.
2. Repeat with the bail **45° back** and **90° back** (toward the back of the head), 5 minutes each.
3. **Re-index with your eyes closed.** Close your eyes. The helper times you. Reach up and move the bail from 0° to 45° back and let go. 10 trials. Then the helper checks the angle against the marks. The helper has drawn tape marks at 0°, 45° and 90° on the bail and the pad.
4. **Lean.** After 20 minutes, rate "how much does the weight pull or lean the helmet?" from 0 (nothing) to 10 (unbearable).
5. **Nuisance.** Rate "how much would having to move this by hand between scratch bouts bother you?" from 0 to 10.

**Pass line (spec S0 row 1, leap4-E)**
- It holds at 0°, 45° and 90° for 20 min with **no creep beyond 3°**.
- Re-index eyes-closed in **under 3 s** in at least 8 of 10 trials.
- Lean **≤ 3/10**.
- "Having to move it" **≤ 3/10**. This is provisional: the real rating comes after the Stage B sessions.

**If it fails**
- **Creeps:** the hinge friction is adjustable. Tighten the hinge's adjustment screw a quarter turn, or try the stiffer Southco E6-10-208-50.
- **Too heavy or leaning:** note the number. The real helmet is lighter than this coin bag; this is the worst case.

**Results sheet S0a-2**

| Item | Result | Pass? |
|---|---|---|
| Hold at 0°, 20 min: creep (°) | | ≤ 3° |
| Hold at 45°, 5 min: creep (°) | | ≤ 3° |
| Hold at 90°, 5 min: creep (°) | | ≤ 3° |
| Eyes-closed re-index, 10 trials: times (s) | , , , , , , , , , | ≥ 8 under 3 s |
| Lean after 20 min (0–10) | | ≤ 3 |
| "Having to move it" (0–10) | | ≤ 3 (provisional) |
| Coin bag mass (g), bail radius (mm) | | |
| Notes | | |

---

## 5. S0a-3: Build the dish bench, about 4 hours

### 5.1 What it is and what it proves

**What it is: a small hand-driven model of the pad's moving heart.**
- **The deck** (D01) is the still part. It stands on three legs whose round feet rest on the ball, or on your head. Its underside has **three dish pockets**.
- **The block** (D02) carries the three nails. It hangs under the deck on **three plastic balls** (the domes), which ride in the pockets. A **lift elastic** pulls the block up so that the balls stay in contact with the pockets.
- **How the pockets work:**
  - In the middle of each pocket the surface is part of a big sphere centred on the centre of the ball, or of your head. Moving there, the block rolls round the ball and the nails keep the same distance from the surface: they press evenly.
  - Near the edges the pocket rises: 34°, then 50°. The block is lifted and the nails come off the skin.
  - The path itself does the lifting. No valve is involved.
- **The C-arm** (D08) is fixed to the block. It reaches out past the deck and back over the top, where two pins (styli) run in the grooves of a **template** (D09–D11) screwed to the deck top. The template sets the path:
  - **T1**, star of lines + 2 off-centre chords;
  - **T2**, D-path: a one-way rake, then a return round the rim with the nails up;
  - **T3**, offset circle.
- **The nails** are spring-loaded:
  - each nail is a resin rod with the spec tip (a Ø 2 mm flat with a rounded rim on a 90° cone), sliding in a guide;
  - a small magnet on a plunger holds it, and a spring above the plunger presses down;
  - if a hair pulls a nail downward with more than about 0.2 N, the magnet lets go and the nail drops out. That is safety condition C1.

**What it proves:**
- (a) the gate geometry: where the nails touch, how far they lift, how steeply they land;
- (b) the sensation on your crown, which is the S0a deciding question;
- (c) the breakaway and the nail profile (C1, C2) on a real part.

### 5.2 Parts for the bench

**Printed parts**
- D01 deck, D02 block, D03 nose plate;
- D04 plunger ×3 (+1 spare), D05 seat disc ×3 (+1);
- nails: D06 N20 ×4, D07 N30 ×4, D16 N35 ×3;
- D08 C-arm, D09 / D10 / D11 templates, D12 skid ring, D13 ball cradle, D15 lift gauge;
- optional: D14 side mock.

**Bought parts and hardware (cart-S0a A)**
- 3 × 6 mm Delrin balls;
- 3 × 3 × 2 mm magnets;
- 3 springs (kit or pen springs);
- steel paper clips;
- **screws:**
  - 3 × M3 × 12 socket screws (nose plate);
  - 3 × M3 × 4 set screws (spring preload);
  - 2 × M3 × 12 (C-arm to block);
  - 2 × M3 × 8 (template to deck);
  - 2 × M3 × 25 socket screws (the styli);
- 1 mm elastic cord or a thin rubber band;
- superglue;
- candle wax or PTFE dry-lube spray;
- the 7 in ball;
- masking tape and washable markers;
- coins.

**Screw holes, explained once.**
- Holes marked "pilot" are **2.6 mm**. An M3 screw cuts its own thread in the plastic the first time: turn it slowly and firmly, and stop as soon as it is snug.
- Do not over-tighten. If a pilot strips, put a drop of superglue in it, wait 10 minutes, and screw in again.
- Holes marked "clear" are 3.4 mm. The screw passes through freely.

### 5.3 Step by step

**D1. Inspect and clean the prints (20 min)**
1. **Deck.** Remove any support or brim. Look into the three pockets (deck upside down). The pocket floors should be smooth, curved surfaces with no blobs or strings. Pick strings out with a toothpick. The legs should be straight. Each foot is a small ball.
2. **Block.** Look into the three bores from the bottom. A Ø 6 mm plunger must slide in and out of each bore **under its own weight**, when you tip the block. If it sticks, wrap 400-grit sandpaper round a pencil and sand the bore lightly, or sand the plunger's outside. Check the three ball sockets on top of the posts are clean half-spheres.
3. **Nose plate.** Hold it vertical. A nail dropped into each guide bore must slide through by its own weight. If it sticks, twist a 3/16 in (4.76 mm) drill bit through the bore **by hand**: no drill motor.
4. **Nails.** Look at each tip under good light. Good is a small flat circle (Ø 2 mm) with a smooth rounded edge, then a cone to the full rod. **Fingernail test:** drag the tip firmly across the back of your hand. It must feel blunt and leave **no scratch line**. If you feel an edge or a burr, sand the rim lightly with 400 grit, rolling the nail between your fingers, then repeat. FDM-printed nails usually need this; resin nails usually do not.
5. **Templates.** Run an M3 × 25 screw, thread first, along every groove. It must slide all the way round without catching. Sand any catch.

**D2. Glue the three balls into the posts (5 min + 10 min cure)**
1. Put one small drop of superglue gel in each socket on top of the block's three posts.
2. Press a Delrin ball into each one with your thumb (wearing a glove) or with a flat piece of wood until it seats.
3. Wipe off any glue that squeezed out. **No glue may stay on the top half of the ball.**
4. **Good:** each ball sticks up about 3.6 mm above its post and cannot be turned with a fingertip.

**D3. Magnets into the plungers (10 min + cure)**
1. Wear glasses. Take **one** magnet at a time out of the bag. They jump to each other and to steel.
2. Put a pin-head drop of superglue into the small round pocket in the **flat end** of a plunger. The cup end is the other end.
3. Drop a magnet in and press it flush with a toothpick. Polarity does not matter.
4. Repeat for 4 plungers. Put the bag of magnets away, sealed.

**D4. Steel tips on the nails (20 min + cure)**
1. Cut 5 mm pieces from a **steel** paper clip: one per nail, 11 in all. Check the clip is steel: a magnet must stick to it. Coated clips are fine.
2. Straighten each piece with pliers. Square one end of each by rubbing it on 400-grit paper laid on a flat table.
3. Dip the other end in superglue and push it fully into the small hole in the **top** of the nail (the ringed end). The squared end must end **flush** with the nail top.
4. After 10 minutes, rub the nail top on the sandpaper on the table, keeping the nail upright, until steel and plastic are flush.
5. Check: a magnet sticks to the top of every nail.

**D5. Springs (15 min)**
1. You need 3 springs that fit inside the plunger's cup (Ø 5.3 mm) and are about 12 mm long when free.
   - **From the kit:** use 0.3 mm wire, 4–5 mm outside diameter, and cut to about 12 mm with side cutters.
   - **Pen springs:** most click-pen springs fit as they are.
2. Make the three springs **the same**: same type, same length. You tune the force in D10.

**D6. Assemble the nail stacks (20 min)**
1. Turn the block upside down on the towel, top down, so the three bore openings face up.
2. Into **each** bore, in this order:
   1. a **seat disc** (it falls to the bottom, which is the top of the bore);
   2. a **spring**;
   3. a **plunger**, cup first, so the cup goes over the spring and the magnet face looks up at you.
3. Lay the nose plate on, counterbores up, with its three screw holes over the block's three screw pilots. Its three guide bores line up with the three plungers.
4. Drive 3 × M3 × 12 screws through the nose plate into the block. Snug, not tight.
5. Turn the block upright. From the top, screw an **M3 × 4 set screw** into the small hole above each bore, using the 1.5 mm hex key, until it is **flush with the block's top surface**. This is the "zero preload" position. Each further full turn adds 0.5 mm of preload. **Never leave a screw standing proud of the top surface**: there is only about 6 mm of clearance to the deck above.
6. **Nails in.** Choose the set for the surface:
   - **N30** (2 rings) for the 7 in ball;
   - **N20** (1 ring) only for a true 170 mm ball;
   - **N35** (3 rings) for your crown if the crown check in §7.2 says so.
   Push each nail, tip down, up through its guide bore from underneath until it clicks onto the magnet. Let go: the nail hangs.
7. **Good:**
   - Each nail hangs straight down.
   - Pushed up with a finger, it slides in smoothly, about 6 mm, against the spring.
   - Released, it comes straight back down.
   - A firm downward tug pops it off the magnet, and it falls out.

**D7. Dish pockets: smooth and lubricate (20 min)**
1. Deck upside down. Wrap 400-grit sandpaper round your fingertip and lightly sand the floor of each pocket, mainly the slopes, until it feels smooth. Blow the dust out.
2. **Wax:** rub an unscented candle firmly over the whole pocket surface, then buff it with a dry cloth until it is slippery. Or spray a light coat of PTFE dry lube and let it dry for 10 minutes.
3. **Check:** set the block in the upside-down deck, balls down into the pockets. Slide it around with a finger. It should glide without grabbing, squeaking or clicking. Clicks mean a rough spot: sand there and wax again.

**D8. The lift elastic (20 min)**
1. **Make a calibration mark.** Cut 15 cm of elastic. Tie one end to a pencil. Hang a paper cup with 30 nickels from the other end (30 × 5.00 g = 150 g, plus the cup; weigh the lot on the scale and add or remove nickels until it reads 150 g). Measure how far the elastic stretches: mark 20 mm of unstretched elastic before hanging, and see what it becomes. Write the ratio down, for example "20 mm → 31 mm at 150 g".
2. **Hook pin.** Push a straight 25 mm piece of paper clip through the small cross-hole near the bottom of the block's central well. It sits across the well like a bar.
3. Tie the elastic around that bar inside the well with a double knot. Pull the free end up out of the well.
4. **Put the ball in the cradle** (D13) on the table. Cover the top of the ball with overlapping strips of masking tape, a patch about 10 cm across. Draw a small cross at the very top.
5. Set the block on the ball, nails down, centred over the cross. The C-arm is not fitted yet.
6. Thread the elastic's free end up through the hole in the **centre of the deck**, from underneath. Lower the deck over the block. The three feet land on the ball; the three balls on the block go up into the three pockets.
7. **Lift the block into the dish.** Pull the elastic up through the deck top. Stretch it until the length between the deck hole and the well bottom is stretched by your calibration ratio (about 150 g of pull).
8. Tie it around a 12 mm piece of toothpick (the **toggle**) and lay the toggle in the slot on the deck top.
9. **Good:**
   - The block hangs up in the dish by itself: the balls touch the pocket floors.
   - The nails rest on the ball and are pushed up a little.
   - When you push the block sideways with a finger, it rolls round under the deck, its edge lifts as it reaches the rims, and the nails come off the ball.

**D9. Breakaway check: the "penny test" (C1), 15 min. Repeat on the day of the scalp session.**

This proves that a hair caught on a nail can never be pulled harder than about 0.25 N. The magnet lets go first.

1. Take the deck off, lifting the block out. Hold the block nose-down with a clamp, or have a helper hold it, about 15 cm above the table.
2. Tie a loop of sewing thread around one nail just above the tip cone, so it cannot slip off. Hang a small paper cup from the thread.
3. Add pennies one at a time (each 2.50 g) until the nail drops off its magnet into the towel.
4. Weigh the cup + pennies + thread on the scale. That weight is the release force. 100 g = 1 N, so 12 g = 0.12 N.
5. Repeat **10 times per nail**.
6. **Pass:** every reading is **12–25 g**.
   - **Over 25 g:** stick one layer of clear tape over that plunger's magnet face (about 0.05 mm) and repeat. A thicker gap weakens the pull.
   - **Under 12 g:** the steel tip is not flat or not flush: re-sand the nail top flat.

**D10. Nail force: the "coin test" (20 min)**

This sets how hard each nail presses: 15–35 g in the working range.

1. Clamp or wedge the block **nose up**: tips pointing at the ceiling. A mug with a cloth works.
2. Make a tiny cradle: a plastic bottle cap with a bit of Blu-Tack in the middle. Weigh it.
3. **On each nail,** with a fine marker, draw a line round the rod exactly where it comes out of the nose plate.
4. Balance the cap on a nail tip, Blu-Tack down. Add nickels (5.00 g) and pennies (2.50 g) one at a time:
   - **F0 (touch-down force):** the total when the nail **first** starts to sink.
   - **F2 (working force):** the total when the line has sunk **2 mm** below the nose plate face (ruler or calipers).
5. **Targets:** **F0 ≥ 12 g** and **F2 = 25–35 g**, all three nails within 5 g of each other.
   - **F2 too low:** turn that nail's top set screw clockwise (more preload), half a turn at a time.
   - **F2 too high, even at zero preload:** the spring is too stiff. Cut one coil off a fresh spring, or try a softer spring.
   - **Never above 45 g** at 2 mm.
6. Write the numbers on the results sheet.

**D11. Template on the deck (5 min)**

With the bench assembled on the ball (D8), lay template **T1** (1 notch on its edge) on the deck top:
- the two clear holes go over the two pilot holes in the deck top;
- the long end points to the side where the C-arm will go (away from the deck's grip post).

Fix it with 2 × M3 × 8 screws.

**D12. Fit the C-arm and drop in the styli (10 min)**
1. The C-arm goes on **after** the deck and template. Hold it by its riser and slide it in sideways from the side opposite the grip post, so that:
   - the **lower bar** passes under the deck rim toward the block;
   - the **top bar** passes over the template, about 3 mm above it.
2. Bring the C-arm's foot flat against the flat **ear** on the side of the block. Its two counterbored holes line up with the ear's two pilot holes.
3. Drive 2 × M3 × 12 screws with the **short end of an L-shaped 2.5 mm hex key**: the riser is in the way of a straight driver. Turn a quarter turn at a time. Snug.
4. **Styli:** drop an M3 × 25 socket screw, thread first, through each of the two holes in the top bar, so that it falls into the template groove below. The screw head rests on the bar. The tip then sits 3 mm above the groove floor: that is designed, nothing to adjust.
5. **Good:**
   - Holding **only the round drive grip** at the bottom of the riser, you can push the arm so that both styli run smoothly along the grooves.
   - The block follows underneath.
   - At the ends of each groove the nails lift off the tape.

**Changing templates (1 min):**
1. Lift both styli out by their heads.
2. Undo the 2 template screws.
3. Slide the template out under the top bar, away from the riser.
4. Slide the next one in and screw it down.
5. Drop the styli back in.

**Taking the block out** (for D9 or D10): remove the styli and the 2 C-arm screws, slide the C-arm out, untie the toggle, and lift the deck off.

**D13. Final dry run (10 min)**
1. Push the grip slowly along each line of T1, end to end, 5 times. Listen: no squeaks or clicks from the dish.
2. Look from the side at eye level. The nails should touch the tape only in the middle part of each stroke and stand clearly off it at both ends.
3. **If the block drops away from the dish at the ends** (the balls leave the pockets): the elastic is too weak. Re-tie it 3 mm shorter.
4. **If the arm is heavy to push:** re-wax the pockets and check the nails are not too strong (D10).

---

## 6. S0a-4: Bench tests on the ball (geometry, C1, C2), about 2 hours

The bench is on the 7 in ball in its cradle, masking tape over the top, with **N30** nails. On a 7 in ball they behave like N20 on the spec's 170 mm ball.

**Predicted results** (`cad/dish_kinematics.py`). These let you tell "the bench works as designed" apart from "the spec has a problem":

| Test | Spec S0 pass line | Predicted for the bench as frozen | Meaning if you get the prediction |
|---|---|---|---|
| G1 ink rake length per nail | ≥ 15 mm | **≈ 10–10.5 mm** | the bench is right; the spec dish is short (CONFLICTS #1) |
| G2 clearance at the stroke ends | ≥ 5 mm | **5.4–5.8 mm** (N30 on the 7 in ball) | pass |
| G3 landing angle | ≤ 35° | **≈ 48–62°** | the bench is right; the spec dish lands steeply (#1) |
| G4 landing spread, mixed nails | ≥ 20 ms | ≈ 2 mm of block travel between the first and last nail | pass if ≥ 1.5 mm |
| G5 breakaway C1 | 0.12–0.25 N | — | must pass |
| G6 slip loop C2 | sheds 10/10 | — | must pass |

**G1 ink rake length (T1 template, 20 min)**
1. Colour the flat of each nail tip with washable marker. Re-ink every 3 strokes.
2. Holding only the drive grip, push the styli slowly (about 2 s per stroke) along the **0° line** of T1, from one end of the groove to the other, 3 times.
3. Each nail leaves a short line on the tape. Measure each line's length along the tape with a ruler, or with calipers, laying them along the curve. Record all three.
4. Turn the whole bench on the ball by 45°, so the feet move round the ball, and repeat on a fresh patch of tape. Do this for 4 headings. You can also use T1's other lines.
5. Bonus: run the two **chord** lines (offset 5 and 9). Their traces should be shorter.

**G2 clearance at the stroke ends (10 min)**
1. Push the styli to the **end** of the 0° line and hold them there.
2. Slide the **lift gauge** (D15) under each nail tip, thinnest step first. Find the thickest step that slides under the tip without touching it (2, 3, 4, 5, 6 or 7 mm). The ball is round, so slide the gauge straight under the tip.
3. Do both ends, and the far point of T3's circle. Record the smallest value for each nail.
4. **Pass:** ≥ 5 mm with N30 on the 7 in ball.
5. Repeat with **N35** nails, the spec's worst reserve. The prediction is about 4 mm: record it, it does not block GO (CONFLICTS #2).

**G3 landing angle (optional, 20 min)**
1. Prop the phone at the height of the nail tips, beside the ball, looking across at the nail on that side. Tape a ruler card behind the nail as a scale.
2. Film in 240 fps slow motion while pushing a 0° stroke inward from the rim, at about one second per stroke.
3. Step frame by frame through the last 2 mm before the tip touches. Over that distance, measure how far the tip moves **down** and how far it moves **along**. Landing angle = atan(down / along).
4. Record it. The prediction is about 50°.

**G4 landing spread (optional, 15 min)**
1. Fit one **N20**, one **N30** and one **N35** nail.
2. Ink the tips and push one slow 0° stroke inward from the rim.
3. The three traces start at different points. Measure how far the stylus had to travel between the first and last nail landing: watch the stylus position in slow motion, or mark it on the template with a pencil as each nail touches.
4. **Pass:** ≥ 1.5 mm (≈ 20 ms at the motor-driven 1.4 Hz).
5. Put the matched set back afterwards (N30 for the ball; your choice from §7.2 for your head).

**G5 breakaway (C1).** Already done in D9. Record the 30 readings.

**G6 slip-loop test (C2, 10 min)**
1. Take 5 long hairs from a hairbrush (yours, or anyone's 10 cm or longer).
2. With the block out of the deck and hanging nose-down, tie a loose slip loop of one hair around a nail **halfway up its exposed rod**.
3. Hold the other end of the hair still on the table. Slowly lift the block 10 mm.
4. **Pass:** the loop slides down and off the tip, 10 out of 10 tries per nail, without the nail coming off its magnet first.
5. Write down any snag, and where on the nail it caught.

**G7 dish noise (5 min).** Run 20 strokes of each template at a brisk pace (about 1.5 strokes per second), with your ear 30 cm away. Note any squeak, click or buzz, and where it happens. If there is any, re-wax.

**G8 side mock (optional, 30 min).** Put the bench on the D14 side mock (the 70 × 150 curved patch) instead of the ball, and repeat G1 and G2 along both directions. Record. This only informs the PAD work package.

### Results sheet S0a-4: bench geometry (print this)

Date: ________  Ball: 7 in / other ______  Nails: N20 / N30 / N35  Template(s): ______

| Test | Nail P0 | Nail P2 | Nail P3 | Pass line | Pass? |
|---|---|---|---|---|---|
| D10 F0 touch-down (g) | | | | ≥ 12 g | |
| D10 F2 at 2 mm (g) | | | | 25–35 g, within 5 g | |
| D9 / G5 breakaway, 10 pulls (g): min / max | / | / | / | 12–25 g | |
| G1 rake 0° (mm) | | | | ≥ 15 (predicted ≈ 10) | |
| G1 rake 45° (mm) | | | | | |
| G1 rake 90° (mm) | | | | | |
| G1 rake 135° (mm) | | | | | |
| G1 chord e = 5 / e = 9 (mm) | / | / | / | shorter than G1 | |
| G2 clearance at the ends, N30 (mm) | | | | ≥ 5 | |
| G2 clearance at the ends, N35 (mm) | | | | record (predicted ≈ 4) | |
| G2 clearance, T3 far point (mm) | | | | ≥ 5 | |
| G3 landing angle (°) | | | | ≤ 35 (predicted ≈ 50) | |
| G4 spread, mixed nails (mm of stylus travel) | — | — | — | ≥ 1.5 | |
| G6 slip loop, sheds out of 10 | | | | 10/10 | |
| G7 noise (none / squeak / click, where) | | | | none | |
| Lift elastic: stretch at home (mm), approx. pull (g) | | | | ≈ 150 g | |

---

## 7. S0a-5: The scalp session, the deciding gate (about 45 min)

**What it proves.** Whether three blunt drafted nails at about 0.3 N each, moved over your crown, feel like **a good scratch**: crisp, not a brush, not pokey. And whether the dish's short, steep rake costs anything compared with a longer hand rake using the same nails.

**People.**
- **Michael** sits, eyes closed, and rates.
- **The helper** runs everything from the script below, and writes down every rating.

### 7.1 Before the session (the helper, 15 min, the same day)
1. **Penny test (D9)** on all 3 nails: every pull 12–25 g. **If any nail fails, there is no session today.**
2. **Coin test (D10):** F2 25–35 g on all 3.
3. **Fingernail test** on all 3 tips: blunt, no scratch line.
4. **Nail count:** 3 on the block, and the spares in a labelled cup.
5. Lay out:
   - both glasses;
   - the bench with template **T1** fitted;
   - templates T2 and T3 nearby;
   - the hand-rake kit: the **second** block assembly if you printed one, or the skid ring D12 and 3 × M3 × 16 screws;
   - the order card (§7.4), the results sheet (§7.5), a pen, a timer, a hairbrush.
6. **Hand-rake setup** (if you only have one block, the helper swaps it during the rests):
   1. Take the block out of the deck.
   2. Swap the 3 nose-plate screws for 3 × M3 × 16 screws that also pass through the skid ring D12, ring under the nose plate.
   3. Keep the C-arm on: the helper holds the block by the C-arm's drive grip.
   4. The three skid feet now rest on the scalp around the nails.

   The swap takes about 3 minutes. Do all the hand-rake (B) bouts together, in the middle of the session, as the order cards do.

### 7.2 Set up on the head (5 min)
1. Michael sits upright in a straight chair. Hair clean, dry and combed, no product. Glasses on, both people.
2. **Choose the nails.** The helper rests the bench gently on the crown and looks from the side: are all 3 nail tips touching the scalp, with each rod pushed up a little?
   - **If a nail hangs free** (crown flatter than the ball): change to **N35** nails.
   - **If a nail is pushed right up and the block tilts** (crown more curved): use N20.
   - Most adult crowns want **N30 or N35**.
3. Michael: "Can you feel all three?" If yes, start.

### 7.3 The helper's script (read it out word for word)

**Start:**
> "I'm going to give you ten short bouts, thirty seconds each, with a rest between. Keep your eyes closed. After each bout I'll ask you seven quick questions. Say 'stop' or lift your hand at any time and I'll lift it straight off."

**Each bout:**
1. Read the next line of the order card. Set up that mode quietly: change template, or change to the hand rake.
2. **For dish modes (A1, A2, A3):**
   1. Rest the bench on the crown by its own weight. Steady it with one hand on the **grip post** on the deck top, without pressing down.
   2. With the other hand, push the **drive grip** along the groove at about 1–1.5 strokes per second for 30 seconds:
      - **A1 (T1 line star):** do 10 strokes on one line, then lift the styli, move to the next line, drop them in, and carry on. All 4 lines, then repeat. This is a slow "precessing line".
      - **A2 (T2 D-path):** set the deck so the straight chord runs **with the grain** (§3 step 7: the way the hair lies). Go round the D in one direction only: chord with the grain, return round the arc.
      - **A3 (T3 circle):** go round the circle steadily. Every 5 turns, rotate the whole bench about 30° on the head (lift, turn, set down).
3. **For hand-rake mode (B):** hold the block by the C-arm grip, skids resting on the crown, nails touching. Stroke about 25 mm back and forth at 1–1.5 strokes per second. **At each end, lift the whole thing about 5 mm**, then set it down again for the return. Change direction by 45° every 10 strokes. Never press: the skids carry the weight.
4. **For reference mode (C):** scratch the same patch with your own fingertips, nails short and clean, a normal friendly scratch, the same pace and the same 30 seconds.
5. At 30 s, lift straight off. Say "rate please" and ask, writing each answer:
   - **Q1** "How satisfying was that, as a good scratch? Zero to ten."
   - **Q2** "Scratch, or brush?" (S / B / unsure)
   - **Q3** "Crisp in both directions, back and forth?" (Y / N; for A2 write "n/a")
   - **Q4** "Pressure: too light, about right, or too hard?" (L / R / H)
   - **Q5** "Any tug, pull, catch or sting?" (Y / N). **If Y: stop, look, and run the stopping rules.**
   - **Q6** "Did it feel like a machine or a person?" (M / P / can't tell)
   - **Q7** "One word for it?"
6. **Count the nails on the block: 3?** Write ✓. Rest 60 s while you set up the next bout.

**End:**
1. "Last one: of everything you felt, which was best and which was worst? Anything to add?"
2. Look at the scalp: any redness? Note it, and check again after 10 minutes.

**Stopping rules (helper).** Lift the bench straight up and stop the session if any of these happen:
- Michael says stop or raises a hand;
- Q5 = Y;
- a nail is missing;
- anything comes loose;
- the bench rocks or tilts on the head;
- hair visibly wraps a nail or skid;
- you are unsure.

**After stopping:**
1. A missing nail is in the hair. Part the hair gently and find it.
2. Inspect the spot.
3. Re-run the penny test on that nail before using it again.

### 7.4 Blind order cards (the helper uses one; Michael never sees it)

Each card has 10 bouts: every dish mode twice, the hand rake twice, the fingertips twice. The order is mixed so that Michael cannot guess. B bouts are kept next to each other because the block swap takes a few minutes. Before the day, the helper picks a card by rolling a die: 1–2 = card 1, 3–4 = card 2, 5–6 = card 3.

| Bout | Card 1 | Card 2 | Card 3 |
|---|---|---|---|
| 1 | A1 | C | A3 |
| 2 | C | A2 | A1 |
| 3 | A3 | A1 | C |
| 4 | A2 | A3 | A2 |
| 5 | B | B | B |
| 6 | B | B | B |
| 7 | A1 | C | A3 |
| 8 | C | A3 | C |
| 9 | A2 | A1 | A2 |
| 10 | A3 | A2 | A1 |

On a second day, use a different card. If the pressure answers say "too light" in 4 or more A bouts, give a half turn more preload on all 3 set screws first. Re-run the coin test: F2 must stay ≤ 45 g.

### 7.5 Results sheet S0a-5: scalp session (print this)

Date: ______  Helper: ______  Card no.: __  Nails: N20 / N30 / N35  F2 today (g): __ / __ / __  Penny test passed: Y / N

| Bout | Mode | Q1 0–10 | Q2 S/B/? | Q3 Y/N | Q4 L/R/H | Q5 tug? | Q6 M/P/? | Q7 word | Nails 3? |
|---|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |
| 9 | | | | | | | | | |
| 10 | | | | | | | | | |

**Summary (fill in after):**

| Mode | Mean Q1 | "Scratch" count | "Crisp both ways" count | Pressure: L / R / H | Tugs |
|---|---|---|---|---|---|
| A1 dish, line star | | /2 | /2 | | |
| A2 dish, D-path | | /2 | n/a | | |
| A3 dish, circle | | /2 | /2 | | |
| **A best mode** | | | | | |
| B hand rake | | /2 | /2 | | |
| C fingertips (yardstick) | | /2 | /2 | | |

Best overall: ______  Worst: ______  Redness after 10 min: none / some (where): ______

---

## 8. S0a decision: GO or NO-GO

Use the summary table. "A" means the dish modes; take the **best** dish mode's mean.

| Outcome | Rule | What you do next |
|---|---|---|
| **GO: dish as built** | best A mean **≥ 6/10**, "scratch" in **≥ 5 of the 6** A bouts, "crisp both ways" on lines, **zero tugs**, all bench "must pass" items pass (D9, D10, G2 with N30, G6) | Buy **cart-S0b**. Send the results sheets to the Director. The short dish rake was good enough; CONFLICTS #1 can be closed as "accept". |
| **GO: concept, dish needs rework** | best A mean < 6, but **B ≥ 6/10** with "scratch" in both B bouts, zero tugs | Buy **cart-S0b**: it does not depend on the dish. Send the Director the A-vs-B difference. That is the evidence for re-scaling the dish (CONFLICTS #1, option b or c) **before** any Stage A pad CAD. |
| **NO-GO** | both A and B < 6/10, **or** "brush" in most bouts, **or** any tug that the C2 nail profile should have prevented | **Do not buy S0b.** Per spec: tip, force and variation work comes first. Use Q4 (pressure), Q7 words and how close C came, to choose between: higher force (F2 40–45 g), a different tip (the 05-engineering tip family), or more variation. Report to the Director. |
| **Fix the bench first** | a "must pass" bench item fails (breakaway out of range, nails sticking, block falling out of the dish, G2 < 4.5 mm with N30) | Fix it (§5 tips) and repeat §6. Not a decision about the concept. |

**The helmet test (§4) does not block S0b.** It feeds the halo work package. If it failed, tell the Director, because powered travel may come back.

**Expected FAILs.** G1 (rake about 10 mm) and G3 (landing about 50°) are predicted by the spec geometry itself. They are **not** reasons for NO-GO. Report the measured numbers: they settle CONFLICTS #1.

---

## 9. S0b-1: Klipper streaming test (spec V-K1), about 5 hours

**What it proves.** That the stock Klipper firmware on the real Stage A controller can do three things:
- drive the three drum motors as extra G-code axes A, B and C (`MANUAL_STEPPER … GCODE_AXIS`, with `kinematics: none`);
- follow the feed rate F;
- stream about 200 short segments per second without stutter, and switch an output (a stand-in for a valve) within **±2 ms** of its planned point on the path, over 500 strokes.

If it does not, the spec's fallback 1 (winch kinematics) or fallback 2 (a custom module) is chosen now, before Stage A.

**Parts:**
- M8P V2.0 + CB1 + heatsink;
- 3 × TMC2209;
- 3 × 17HS08 motors, which can sit loose on the table for this test;
- 24 V adapter + pigtail + mains cord;
- microSD;
- logic analyser + test hooks;
- 1 LED + one 330 Ω resistor + Dupont jumpers;
- your Mac on the same Wi-Fi.

**Files:** `klipper/printer.cfg`, `klipper/s0_stream.py`, `klipper/k_timing.py`.

**Software (free):**
- balenaEtcher or Raspberry Pi Imager, to write the SD card;
- PulseView (sigrok.org), for the logic analyser;
- a web browser.

**Where a step says [VERIFY], follow the BTT document.** BTT changes details between board revisions. Do not guess pins or jumpers. The BTT documents to use:
- the Manta M8P V2.0 user manual and pin diagram: github.com/bigtreetech/Manta-M8P, folder V2.0;
- the CB1 guide: github.com/bigtreetech/CB1.

**K1. SD card for the CB1 (20 min)**
1. Download the latest **CB1 OS** image from github.com/bigtreetech/CB1 → Releases. Choose the one with Klipper, Moonraker and Mainsail preinstalled [VERIFY name].
2. Write it to the microSD with balenaEtcher.
3. Re-insert the card in the Mac. Open the small **BOOT** drive and edit `system.cfg` with TextEdit:
   - set `WIFI_SSID` and `WIFI_PASSWD` to your Wi-Fi;
   - save, and eject.

**K2. Prepare the board (power OFF, adapter unplugged, 30 min)**
1. **CB1 onto the M8P.** Line the CB1 up over the two board-to-board connectors and press evenly until it seats. Stick the heatsink on the CB1's processor. Push the microSD into the CB1's slot.
2. **Driver jumpers for S0b.**
   - Under the MOTOR1, MOTOR2 and MOTOR3 sockets, set **UART mode**: one jumper per socket, as the M8P V2.0 manual shows [VERIFY].
   - UART lets Klipper set the motor current to 0.35 A in software, so S0b needs no multimeter.
   - **In Stage A you change to standalone mode with the current set by the VREF screw.** That is spec C20, a hardware current cap, and it needs a multimeter.
3. **Drivers.** Fit the heatsinks to 3 × TMC2209. Plug them into MOTOR1–3 with the **EN pin matching the EN mark on the board.** Check twice: reversed = dead driver.
4. **Motors.** Plug motor A into MOTOR1, B into MOTOR2, C into MOTOR3. Label the motor leads now with masking tape: A, B, C.
5. **LED (the stand-in valve).**
   - On the board's expansion or probe header, pick a free 3.3 V GPIO pin and a GND pin [VERIFY which pins are free in the BTT pin diagram].
   - Wire: GPIO pin → 330 Ω resistor → LED long leg; LED short leg → GND. Use Dupont jumpers; the resistor and LED legs push into the jumper ends.
   - **Do not use a FAN output.** It switches 24 V, which would destroy the logic analyser.
6. **Power.**
   - The barrel-jack pigtail's red wire goes to **VIN +** and black to **VIN −**, in the board's power screw terminal. Tighten the screws; tug-test each wire.
   - Set the driver-power selection so the drivers take 24 V from VIN [VERIFY jumper in the manual].

**K3. First power-on (10 min)**
1. Plug in the adapter. The board LEDs light.
2. Wait 2 minutes. In the Mac's browser go to `http://BTT-CB1.local`, or find the CB1's IP address in your router's device list. Mainsail opens. It will say Klipper cannot connect to the MCU: that is expected, the firmware comes next.

**K4. Klipper firmware on the board (45 min)**
1. On the Mac, open Terminal and run `ssh biqu@BTT-CB1.local`. The password is in the CB1 guide [VERIFY].
2. Run `cd ~/klipper && make menuconfig` and set:
   - Enable extra low-level configuration options;
   - Micro-controller: STM32;
   - Processor: STM32H723;
   - Bootloader offset: 128KiB;
   - Clock reference: 25 MHz crystal;
   - Communication interface: USB (on PA11/PA12).

   [VERIFY every line against the M8P V2.0 manual's "Klipper firmware" section.] Press Q, then Y, to save.
3. Run `make`. It should end without errors and create `out/klipper.bin`.
4. Flash the board exactly as the M8P V2.0 manual describes, either:
   - DFU mode, holding the BOOT button while pressing RESET, then `make flash FLASH_DEVICE=0483:df11`; or
   - the board's own SD-card method, if V2.0 has one [VERIFY].
5. Run `ls /dev/serial/by-id/` and copy the line starting `usb-Klipper_stm32h723…`.

**K5. Load the configuration (30 min)**
1. In Mainsail: Machine (folder icon) → `printer.cfg` → replace all text with `klipper/printer.cfg` from this package.
2. Paste the serial id from K4 into `[mcu] serial:`.
3. Replace every `<…>` with the pin name from BTT's sample config for the M8P V2.0:
   - MOTOR1 / 2 / 3 STEP, DIR, EN and UART pins;
   - your LED GPIO.

   Copy them exactly; do not guess.
4. SAVE & RESTART. **Good:** Mainsail shows "Klipper ready" with no red message.

**K6. First moves (20 min)**
1. Stick a tape flag on each motor shaft.
2. In the Mainsail console type `AXES_ON`. The motors hum quietly: they are energised.
3. Type `G1 A10 F600`. **Motor A turns about a quarter turn (≈ 95°).** Type `G1 A0 F600`: it turns back.
4. Repeat with `B` and `C`.
5. `SET_PIN PIN=valve_led VALUE=1` → the LED lights. `VALUE=0` → off.
6. **If the console says the A/B/C axis is unknown or not allowed,** write down the exact message: that is the V-K1 answer. Skip to K10 and record it as a FAIL.

**K7. Make the test files (10 min)**

On the CB1 (in the ssh window) or on the Mac, in the `klipper/` folder of this package, run:
```
python3 s0_stream.py line  --strokes 500 --hz 1.4 --amp 16 --psi 90 > line14.gcode
python3 s0_stream.py line  --strokes 500 --hz 2.0 --amp 16 --psi 90 > line20.gcode
python3 s0_stream.py pline --strokes 120 --hz 2.0 --amp 16          > pline20.gcode
python3 s0_stream.py line  --strokes 500 --hz 1.4 --psi 90 --dry      # prints planned duration and segments/s
```
Write down the planned durations. Upload the three `.gcode` files in Mainsail (G-Code Files → Upload).

**K8. Wire the logic analyser (15 min)**
1. Connect the analyser's GND to a board GND pin.
2. **CH0** goes to the LED's GPIO pin (the same pin as the resistor).
3. **CH1** goes to the **DIR** pin of the MOTOR1 driver. Use a test hook on the driver module's DIR pin [VERIFY pin position in the TMC2209 V1.3 pinout].
4. Plug the analyser into the Mac. In PulseView: driver "fx2lafw", sample rate **500 kHz**, sample count long enough for 200 s (100 M samples).

**K9. Run and measure (60 min)**
1. Start the capture, then press **Print** on `line14.gcode`. The motors run for about 3 minutes; the LED blinks once per stroke.
2. When it finishes, stop the capture. File → Export → CSV.
3. On the Mac, in the `klipper/` folder: `python3 k_timing.py capture.csv --samplerate 500000`. It prints the delay from each stroke reversal to the LED switching on, and how much that delay **varies** over all strokes.
4. Repeat with `line20.gcode`, which runs near 200 segments per second at mid-stroke.
5. Run `pline20.gcode` without capture. Watch the Mainsail console for any red message ("Timer too close", "Move queue overflow"). Listen: the motors should sound smooth and regular, with no knocks or pauses.
6. Compare each file's actual print time (Mainsail shows it) with the planned duration.

**K10. Pass line (V-K1)**
- **G1 A / B / C** moves are accepted and run.
- Actual print time within **1 %** of planned, for all three files. That means F is followed.
- Timing spread **≤ 4 ms** (= ±2 ms) over **≥ 500 strokes**, at both 1.4 Hz and 2.0 Hz.
- Full-cycle time within 1 % of 714 ms (1.4 Hz) and 500 ms (2.0 Hz).
- `pline20` runs with **no console errors and no audible stutter**.

**If it fails:**
- Write down the exact messages and numbers, and send them to the Director.
- The spec's fallback 1 is Klipper's `winch` kinematics with XY moves. It is a firmware work-package job, not yours.
- The hardware does not change.

### Results sheet S0b-1: Klipper (print this)

| Item | Result | Pass line | Pass? |
|---|---|---|---|
| `AXES_ON` / `G1 A10 F600` accepted? Any error text | | accepted | |
| line14: planned / actual duration (s) | / | within 1 % | |
| line14: delay spread (ms), strokes analysed | , | ≤ 4 ms, ≥ 500 | |
| line14: median full cycle (ms) | | 714 ± 7 | |
| line20: planned / actual duration (s) | / | within 1 % | |
| line20: delay spread (ms), strokes | , | ≤ 4 ms, ≥ 500 | |
| line20: median full cycle (ms) | | 500 ± 5 | |
| pline20: console errors? stutter? | | none | |
| Klipper version (Mainsail → Machine → System) | | — | |

---

## 10. S0b-2: Tendon ink rig (leap4-D L1 (e)), about 6 hours

**What it proves.** That three thin cables in 1.6 m housings, wound by three drums in the box, copy a path to the pad accurately and quietly. This is the "puppet" of spec §4.4. The pen plate stands in for the pin block, and the pen draws what the block would do.

**Parts:**
- **printed:** T01 drums ×3, T02 motor tables ×3, T03 stop blocks ×3, T05 rig deck, T06 pen plate (+ T04 sleeves ×3 if you test housing B);
- **bought:** cart-S0b B and C, plus the S0b-1 controller set-up;
- **hardware:**
  - 12 × M3 × 8 (motors);
  - 3 × M3 × 6 set screws + 3 × M3 nuts (drums);
  - 3 × M3 × 12 + 3 × M3 washers (pen-plate posts);
  - about 16 wood screws;
- **household:** a felt-tip pen, paper, tape, 10 nickels in a small bag (50 g), thread.

**Layout on the plywood** (2 × 2 ft, seen from above; the back edge is the edge farthest from you):
- **Motor row.** Three motor tables in a row, 90 mm apart centre to centre, their centres 80 mm in from the back edge. Left to right: A, B, C.
- **Stop row.** In front of each drum, a stop block 50 mm away. Its hole lines up with the cable as it leaves the side of the drum. Stretch a thread from the drum's edge straight forward to place it.
- **Rig deck.** The rig deck ring sits on a taped sheet of paper near the front edge, in the middle.
- **Housings.** Each 1.6 m housing runs from its stop block, round one big loop on the board, to its stop on the rig deck. Tape the loops down with masking tape:
  - cable **A** goes to the rig deck stop at the **back** (90°);
  - **B** to the front-left (210°);
  - **C** to the front-right (330°).

**Build**

**R1. Motors (20 min).** Each motor goes **under** its table with the shaft sticking up through the big hole. Fix it with 4 × M3 × 8 through the table top into the motor face. The lead points to the back.

**R2. Drums (20 min).**
1. Push an M3 nut into the slot in the drum hub, from the hub's bottom face.
2. Screw an M3 × 6 set screw into the side hole until it reaches the nut.
3. Slide the drum, hub first, onto the shaft until it is 1 mm above the table.
4. Turn the drum so that the set screw faces the flat on the shaft, and tighten with the 1.5 mm key.
5. **Good:** the drum does not slip when you hold it and twist the motor.

**R3. Fix tables and stop blocks (30 min).** Screw them to the plywood with wood screws, as in the layout.

**R4. Cables (60 min).**

**Wear glasses: cut cable ends are sharp.**

Each cable is two pieces, joined by a series spring at the box end.
1. **Piece 1** (drum → spring), 350 mm long:
   1. Push one end in along the lower groove (groove A, next to the hub), through the small axial hole in the hub-side flange, so it comes out on the motor side of the flange.
   2. Slip on a crimp sleeve, crimp it twice with the crimper, and pull back so the sleeve sits in its little pocket.
   3. Wind the cable **1.5 turns** into the groove, in the direction that sends it off the drum straight toward its stop block.
   4. At the far end make a **loop** through one end-hook of a series spring: thread through the hook, back through a crimp sleeve, pull to a 3 mm loop, crimp twice.
2. **Piece 2** (spring → pen plate), 1.85 m long:
   1. Loop and crimp one end through the spring's other hook in the same way.
   2. Thread the free end through the stop block's small hole from the drum side, then into the housing.
3. **Housing:**
   1. Cut 3 × 1.6 m of 4 mm housing with sharp side cutters, making a straight cut.
   2. Open the squashed liner at each end with a pin, and fit a ferrule on each end.
   3. Push the cable all the way through.
   4. Seat one ferrule in the stop block's big hole, and the other in the rig deck stop's big hole. The cable comes out of the rig deck stop toward the centre.

**R5. Pen plate (20 min).**
1. Screw 3 × M3 × 12 screws into the three post holes, leaving about 8 mm standing, each with a washer under the head.
2. Put three marbles in the cups.
3. Wrap tape round the pen until it slides up and down freely in the Ø 12 collar without wobble. Drop it in so its tip rests on the paper.
4. Bring each cable to its post. Wrap it twice clockwise round the screw under the washer, pull until just straight, and tighten the screw onto the washer to clamp it.
5. Label the cables at the posts: A, B, C.

**R6. Pretension and centre (30 min).**
1. Draw a cross in the middle of the paper and set the pen on it.
2. Power on. `AXES_ON`. Each motor now holds its drum.
3. Wind each cable in, in small steps (`G1 A-0.2 F60`, then `A-0.4`, …), until its **series spring is 0.9 mm longer** than when free. Measure with calipers: about 17.8 → 18.7 mm. At 1.65 N/mm this is 1.5 N, the spec pretension.
4. If the pen walks off the cross, pay out a little on the cable it moved toward and wind in the opposite one.
5. When all three springs read 18.7 mm and the pen is on the cross, type `AXES_ON` again. This sets this pose as zero.
6. **Direction check:** `G1 A2 F300`. Cable A pays out 2 mm, so the pen should move **away** from stop A. If it moves toward A:
   1. Power off.
   2. In printer.cfg, add or remove the `!` in front of cable A's `dir_pin`.
   3. Save and restart.

   Check B and C the same way. Return everything to `G1 A0 B0 C0 F300`.

**Tests.** Use a fresh piece of paper for each and label each trace. Make each file with `s0_stream.py` as in K7, then upload and print it.

**T1. Straight lines (bow).**
1. Files: `line --psi 90 --strokes 10 --hz 1.0`, then `--psi 210`, `--psi 330` and `--psi 0`.
2. Lay a steel ruler along each trace. The biggest gap between the ruler and the line is the **bow**: **pass ≤ 0.5 mm**.
3. Also measure each trace's length: it should be **32 ± 0.5 mm**.

**T2. Circles (flats).**
1. File: `circle --radius 11.5 --offset 0 --revs 5 --hz 1.0`.
2. Draw the true circle with a compass: radius 11.5 mm, centred on the cross. Where each cable reverses (6 places), the inked circle may have a small **flat or notch**. Measure the deepest flat inward from the compass circle.
3. Then re-make the file with `--deadband b,b,b`, starting with b = 2 × the deepest flat in mm, and print again. Adjust per cable until **every flat ≤ 0.3 mm**.
4. Record the final b values: Stage A uses them.

**T3. Shrink under load.**
1. Pen at the centre, at rest. Tie a thread to the pen collar, run it flat across the paper and over the board's edge, and hang the 50 g bag of nickels (0.49 N).
2. Dot with the pen before hanging (lift it and drop it), then after. The distance between the dots is the **shrink**: **pass ≤ 0.5 mm**.
3. Repeat pulling in three directions, each halfway between two cables.

**T4. Drift across housing coils.**
1. Print `line --psi 0 --strokes 4` with the housings in 1 loop.
2. Without touching anything else, re-tape all three housings into 1.5 loops, then 2 loops (tighter coils), printing the same file on the same paper each time.
3. The midpoints of the traces must lie within **0.5 mm** of each other.

**T5. Speed.** Print `pline --strokes 60 --hz 1.4`, then `--hz 2.0`. The rosette (a flower of lines) should look even, with no jumps, gaps or stutters.

**T6. Housing B (optional).** Swap one cable's housing for the thin 2 mm coil (1 m piece), using T04 sleeves in both seats, and repeat T1–T4 along that cable. The shorter length is a known compromise: record it and compare.

**T7. Earplug test (noise on the head, 20 min).**
1. Take the pen out. Tape the rig deck ring onto the top of the bike helmet, with the pen plate sitting on its marbles on a piece of card taped inside the ring.
2. Michael wears the helmet and foam earplugs, eyes closed.
3. The helper flips a coin 10 times: heads = start `pline --hz 1.4` for 10 s, tails = do nothing for 10 s. Each time Michael says "running" or "not running".
4. **Pass: ≤ 6 of 10 correct**, which is no better than guessing.
5. Then once without earplugs: note any creak, hum or tick.

### Results sheet S0b-2: ink rig (print this)

| Test | Result | Pass line | Pass? |
|---|---|---|---|
| Spring length free / pretensioned (mm), A / B / C | / / | +0.9 mm each | |
| T1 bow at ψ 90 / 210 / 330 / 0 (mm) | / / / | ≤ 0.5 | |
| T1 trace length (mm) | | 32 ± 0.5 | |
| T2 deepest flat, uncompensated (mm) | | record | |
| T2 deepest flat, compensated (mm); b values A / B / C | ; / / | ≤ 0.3 | |
| T3 shrink at 0.5 N, three directions (mm) | / / | ≤ 0.5 | |
| T4 drift between 1 / 1.5 / 2 loops (mm) | | ≤ 0.5 | |
| T5 rosette at 1.4 and 2.0 Hz even? | | yes | |
| T6 housing B results (optional) | | compare | |
| T7 earplug A/B correct out of 10 | | ≤ 6 | |
| T7 sounds heard without earplugs | | record | |

---

## 11. S0b decision

| Outcome | Rule | Next |
|---|---|---|
| **GO to Stage A** | V-K1 passes (§9) **and** the ink rig passes T1–T4 and T7 | Stage A cart (spec Cart 2, minus everything already bought in S0b: see cart-S0b "carries forward"). Re-print T01 drums in SLA for Stage A. |
| **Klipper fails** | any V-K1 line fails | Send the error text and numbers to the Director. The spec's fallback 1 (`winch` kinematics) or fallback 2 (custom module) is chosen. The board stays. |
| **Tendon fails** | bow, flats or drift over the line after compensation, or audible on the head | Per spec: keep tendons for lines only and restrict circles to R ≤ 8–10, or revisit the drive. Try housing B first if A failed on flats. |

---

## Appendix A. What to send the Director after S0a and S0b

**After S0a:**
- photos of the four filled results sheets (S0a-1, S0a-2, S0a-4, S0a-5);
- one photo of the G1 ink traces next to a ruler;
- the slow-motion clip from G3, if you made one.

**After S0b:**
- results sheets S0b-1 and S0b-2;
- the `k_timing.py` printout;
- photos of the T1 and T2 traces with a ruler;
- the final dead-band values.

## Appendix B. Troubleshooting quick list

**Dish bench**

| Symptom | Likely cause | Fix |
|---|---|---|
| Nail does not come back down after being pushed up | Bore or guide too tight, or spring missing | Sand the bore (D1); check the spring is in the cup |
| Nail falls off by itself | Magnet missing, or the steel tip not flush | D3 / D4 |
| The block clunks at the stroke ends | Elastic too weak: the balls leave the pockets | Re-tie the elastic shorter (D8) |
| Squeak in the dish | Dry spot | Re-wax (D7) |
| The C-arm is hard to push sideways | Pushing at the top bar, or the styli binding in a rough groove | Push at the low grip only; sand the groove |

**Ink rig**

| Symptom | Likely cause | Fix |
|---|---|---|
| Pen trace has random wiggles | Pen loose in the collar | More tape on the pen |
| Pen trace jumps | Cable slipping on its post | Re-clamp under the washer |
| Motor hums but does not turn | Run current too low | In printer.cfg raise `run_current` to 0.45 A; never above 0.6 A |
| Drum slips on the shaft | Set screw not on the flat | Turn the drum until the screw faces the flat, then re-tighten (R2) |

**Klipper**

| Symptom | Likely cause | Fix |
|---|---|---|
| "mcu 'mcu': Unable to connect" | Wrong serial id, or firmware not flashed | Redo K4 / K5 |
