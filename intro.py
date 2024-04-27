import consts


def intro() -> str:
    return r"""
.   _________         .    .
.  (..       \_    ,  |\  /|
.   \       O  \  /|  \ \/ /
.    \______    \/ |   \  /          _                 _  _   _      _
.       vvvv\    \ |   /  |      ___| |__   ___   __ _(_)| \ | | ___| |_
.       \^^^^  ==   \_/   |     / __| '_ \ / _ \ / _` | ||  \| |/ _ \ __|
.        `\_   ===    \.  |     \__ \ | | | (_) | (_| | || |\  |  __/ |_
.        / /\_   \ /      |     |___/_| |_|\___/ \__, |_||_| \_|\___|\__| %s
.        |/   \_  \|      /                      |___/
.               \________/      Distributed YaneuraOu analysis for lishogi
""".lstrip() % consts.SN_VERSION
