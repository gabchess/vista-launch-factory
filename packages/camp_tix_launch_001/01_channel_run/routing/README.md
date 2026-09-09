# Local route receipts

Run `python3 packages/camp_tix_launch_001/01_channel_run/route_packets.py` from the repository root. It checks every portable request against the actual release workspace and writes the route projections here.

The generated JSON files contain host-specific absolute paths and stay outside Git and the handoff archive. Review bindings retain their context digests. The request files, selected fact bytes and original voice guides are included so the recipient can regenerate these receipts on their own machine.
