"""scrapli.docs.generate"""
import pdoc
from pdoc import _render_template, tpl_lookup

context = pdoc.Context()
module = pdoc.Module("scrapli_community", context=context)
pdoc.link_inheritance(context)
tpl_lookup.directories.insert(0, "docs/generate")

# maybe will add api docs for this but not for now!
doc_map = {
}


def recursive_mds(module):  # noqa
    """Recursively render mkdocs friendly markdown/html"""
    yield module.name, _render_template("/mkdocs_markdown.mako", module=module)
    for submod in module.submodules():
        yield from recursive_mds(submod)


def main():
    """Generate docs"""
    for module_name, html in recursive_mds(module=module):
        if module_name not in doc_map.keys():
            continue

        doc_map[module_name]["content"] = html

    for module_name, module_doc_data in doc_map.items():
        if not module_doc_data["content"]:
            print(f"broken module {module_name}")
            continue
        with open(f"docs/api_docs/{module_doc_data['path']}.md", "w") as f:
            f.write(module_doc_data["content"])


if __name__ == "__main__":
    main()
