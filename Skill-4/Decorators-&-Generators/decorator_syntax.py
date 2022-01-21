from rich import print as rprint

def text_color(func):
    def wrapper():
        rprint("[blue] *************************************************************************[/blue]")
        func()
        rprint("[blue] *************************************************************************[/blue]")
    
    return wrapper

from rich import print as rprint
@text_color
def banner():
    rprint(
        " [blue]*[/blue] IOSv is strictly limited to use for evaluation, demonstration and IOS [blue]*[/blue]\n",
        "[blue]*[/blue] education. IOSv is provided as-is and is not supported by Cisco's     [blue]*[/blue]\n",
        "[blue]*[/blue] Technical Advisory Center. Any use or disclosure, in whole or in part,[blue]*[/blue]\n",
        "[blue]*[/blue] of the IOSv Software or Documentation to any third party for any      [blue]*[/blue]\n",
        "[blue]*[/blue] purposes is expressly prohibited except as otherwise authorized by    [blue]*[/blue]\n",
        "[blue]*[/blue] Cisco in writing.                                                     [blue]*[/blue]",
    )

banner()