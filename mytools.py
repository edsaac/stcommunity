from typing import Union

def build_badges(
    repo:str = None, 
    post:str = None, 
    pypi:str = None,
    stcloud:str = None) -> str:
    '''
    Builds a set of badges
    
    '''

    md = """"""
    if repo:
        md += f"""<a href="{repo}"><img src="https://img.shields.io/static/v1?label=:&message=Source%20code&color=informational&logo=github"></a>"""
    if post:
        md += f"""<a href="{post}"><img src="https://img.shields.io/static/v1?label=:&message=Discussion%20post&color=red&logo=discourse"></a>"""
    if pypi:
        md += f"""<a href="{pypi}"><img src="https://badgen.net/pypi/v/{pypi}"></a>"""
    if stcloud:
        md += f"""<a href="{stcloud}"><img src="https://img.shields.io/static/v1?label=:&message=Open%20in%20Streamlit&color=pink&logo=streamlit"></a>"""
    md += """"""
    return md

if __name__ == "__main__":
    pass