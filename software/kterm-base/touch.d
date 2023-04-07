module software.kterm_base.touch;

import std.stdio;

void main(string[] args) {
	if (!(args.length >= 2)) {
		return;
	}

	File n = File(args[1], "w");

	if (args.length >= 3) {
		n.write(args[2]);
	}
	n.close();
}