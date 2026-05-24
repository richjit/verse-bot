def test_bot_module_imports():
    import bot
    assert hasattr(bot, "client")
    assert hasattr(bot, "tree")


def test_embed_color_constant():
    import bot
    assert bot.EMBED_COLOR == 0x7C3AED


def test_links_view_has_three_buttons():
    import bot
    view = bot.LinksView()
    buttons = [c for c in view.children if hasattr(c, "url")]
    assert len(buttons) == 3


def test_links_view_urls():
    import bot
    view = bot.LinksView()
    urls = {c.url for c in view.children if hasattr(c, "url")}
    assert "https://runwiseai.app/" in urls
    assert "https://x.com/useverseai" in urls
    assert "https://x.com/realthomasgu" in urls
