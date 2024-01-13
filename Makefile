all:
	cd builder;
	CURRENT_VERSION=$$(ls draft-lincla-netconf-yang-library-augmentation-??.xml | sort | tail -n 1);\
	echo "CURRENT_VERSION=$$CURRENT_VERSION"; \
	LOCALE="LANG_C" xml2rfc $$CURRENT_VERSION; \
	PREVIOUS_VERSION=$$(ls draft-lincla-netconf-yang-library-augmentation-??.xml | sort | tail -n 2 | head -n 1); \
	rfcdiff $$(basename $$PREVIOUS_VERSION .xml).txt $$(basename $$CURRENT_VERSION .xml).txt