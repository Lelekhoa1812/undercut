.PHONY: check test evaluate bundle
check:
	python3 scripts/undercut.py check

test:
	python3 -m unittest discover -s tests -v

evaluate:
	python3 scripts/evaluate_cases.py --check

bundle:
	python3 scripts/undercut.py bundle --output dist/undercut-skill.zip
