all:
	cd builder; python3 build_yanglib_augment_draft.py
	CURRENT_VERSION=$$(ls draft-ietf-netconf-yang-library-augmentedby-??.xml | sort | tail -n 1);\
	echo "CURRENT_VERSION=$$CURRENT_VERSION"; \
	LOCALE="LANG_C" xml2rfc --v3 $$CURRENT_VERSION; \
	PREVIOUS_VERSION=$$(ls old_draft_version/draft-ietf-netconf-yang-library-augmentedby-??.xml | sort | tail -n 1 | head -n 1); \
	PREVIOUS_VERSION_NAME=$$(basename $$PREVIOUS_VERSION .xml);\
	FILEPATH=old_draft_version/;\
	iddiff $$FILEPATH$(addsuffix .txt, $$PREVIOUS_VERSION_NAME) $$(basename $$CURRENT_VERSION .xml).txt > rfcdiff.html
