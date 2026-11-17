const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

function createElement() {
	const attributes = new Map();
	return {
		listeners: new Map(),
		dataset: {},
		value: "",
		textContent: "",
		hidden: false,
		classList: {
			add() {},
			remove() {}
		},
		addEventListener(type, callback) {
			this.listeners.set(type, callback);
		},
		setAttribute(name, value) {
			attributes.set(name, value);
		},
		getAttribute(name) {
			return attributes.get(name) || null;
		},
		append() {},
		querySelector() {
			return createElement();
		}
	};
}

function preparePage(sourcePath) {
	const source = fs.readFileSync(sourcePath, "utf8");
	const html = source.match(/HTML = r'''([\s\S]*?)'''/)[1];
	const script = html.match(/<script>([\s\S]*?)<\/script>/)[1];
	const elements = new Map();
	const document = {
		querySelector(selector) {
			if (!elements.has(selector)) elements.set(selector, createElement());
			return elements.get(selector);
		},
		querySelectorAll() {
			return [];
		}
	};
	const context = {
		document,
		window: {
			setInterval() {},
			location: {}
		},
		fetch: async () => ({
			ok: false,
			status: 503,
			json: async () => ({ error: "Not configured for test." })
		})
	};
	vm.runInNewContext(script, context);
	return document;
}

for (const sourcePath of [
	path.resolve(__dirname, "..", "Retchan.py"),
	path.resolve(__dirname, "..", "..", "Retchan.py")
]) {
	test(`calculates proposed score divisions in ${path.basename(path.dirname(sourcePath))}`, () => {
		const document = preparePage(sourcePath);
		const form = document.querySelector("#score-calculator");
		const result = document.querySelector("#score-preview-result");
		const submit = form.listeners.get("submit");
		const event = { preventDefault() {} };
		document.querySelector("#score-game").value = "Fortnite";
		document.querySelector("#score-wins").value = "8";
		document.querySelector("#score-draws").value = "0";
		document.querySelector("#score-losses").value = "4";
		submit(event);
		assert.match(result.textContent, /24 proposed points \(Division 9\)/);
		assert.match(result.textContent, /4 losses/);

		const divisionBoundaries = [
			[25, "Division 8"],
			[50, "Division 7"],
			[75, "Division 6"],
			[100, "Division 5"],
			[125, "Division 4"],
			[150, "Division 3"],
			[175, "Division 2"],
			[200, "Division 1"]
		];
		for (const [points, division] of divisionBoundaries) {
			document.querySelector("#score-wins").value = "0";
			document.querySelector("#score-draws").value = String(points);
			submit(event);
			assert.match(result.textContent, new RegExp(`${points} proposed points \\(${division}\\)`));
		}
		assert.match(result.textContent, /not saved or verified/);
		document.querySelector("#score-draws").value = "-1";
		submit(event);
		assert.equal(result.textContent, "Enter whole, non-negative match totals.");
		assert.equal(result.dataset.error, "true");
	});
}
