import json
import os.path
import subprocess
from typing import List

from jinja2 import Environment, FileSystemLoader, select_autoescape

BUILDER_DIR = os.path.dirname(os.path.abspath(__file__))
YANG_DIR_RFC7895 = os.path.join(os.path.dirname(BUILDER_DIR), "yang_augment_RFC7895")
YANG_DIR_RFC8525 = os.path.join(os.path.dirname(BUILDER_DIR), "yang_augment_RFC8525")


env = Environment(
    loader=FileSystemLoader(BUILDER_DIR),
    autoescape=select_autoescape("xml")
)


def _execute_pyang(options: List[str], filenames: List[str], yang_dir: str):
    options += ["-p", yang_dir]
    args = ["pyang"] + options + filenames
    result = subprocess.run(args, capture_output=True, text=True)
    print()
    print("******************************************************")
    print(" ".join(args))
    print("******************************************************")
    print(" ERRORS ")
    print(result.stderr)
    print("******************************************************")
    print(" OUT ")
    print(result.stdout)
    print("******************************************************")
    return result.stderr, result.stdout


def _build_tree(filenames, yang_dir):
    return _execute_pyang(["-f", "tree", "--tree-line-length", "69"], filenames, yang_dir)


def _format_yang(filenames, yang_dir):
    return _execute_pyang(["--ietf", "-f", "yang",
                           "--yang-canonical",
                           "--yang-line-length", "69"], filenames, yang_dir)


def _find_yang_file(prefix: str, yang_dir):
    for yang_file in os.listdir(yang_dir):
        if yang_file.startswith(prefix) and yang_file.endswith("yang"):
            return os.path.join(yang_dir, yang_file)
    raise Exception(f"Yang file with prefix {prefix} not found.")


YANGLIB_AUGMENT_RFC7895 = _find_yang_file("ietf-yang-library-rfc7895-augmentedby", YANG_DIR_RFC7895)
YANGLIB_AUGMENT_RFC8525 = _find_yang_file("ietf-yang-library-augmentedby", YANG_DIR_RFC8525)


def draft_content():
    pyang_results = {
        "yanglib_augment_rfc7895_tree": _build_tree([YANGLIB_AUGMENT_RFC7895], YANG_DIR_RFC7895),
        "yanglib_augment_rfc7895_yang": _format_yang([YANGLIB_AUGMENT_RFC7895], YANG_DIR_RFC7895),
        "yanglib_augment_rfc8525_tree": _build_tree([YANGLIB_AUGMENT_RFC8525], YANG_DIR_RFC8525),
        "yanglib_augment_rfc8525_tree": _format_yang([YANGLIB_AUGMENT_RFC8525], YANG_DIR_RFC8525),
        }
    errors = []
    contents = {}
    for key, (error, output) in pyang_results.items():
        contents[key] = output.strip()
        if error != "":
            errors.append(key + "\n" + error)
    if errors:
        for error in errors:
            print("*******************ERROR********************")
            print(error)
        exit(1)
    return contents


if __name__ == '__main__':
    output = os.path.join(os.path.dirname(BUILDER_DIR), "draft-ietf-netconf-yang-library-augmentedby-03.xml")
    draft_text = env.get_template("draft-ietf-netconf-yang-library-augmentedby.xml")
    with open(output, 'w') as xml_generated:
        xml_generated.write(draft_text.render(**draft_content()))
