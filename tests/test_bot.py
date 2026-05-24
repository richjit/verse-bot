import asyncio


def test_bot_module_imports():
    import bot
    assert hasattr(bot, "client")
    assert hasattr(bot, "tree")


def test_embed_color_constant():
    import bot
    assert bot.EMBED_COLOR == 0x7C3AED


def test_links_view_has_three_buttons():
    import bot

    async def check():
        view = bot.LinksView()
        buttons = [c for c in view.children if hasattr(c, "url")]
        assert len(buttons) == 3

    asyncio.run(check())


def test_links_view_urls():
    import bot

    async def check():
        view = bot.LinksView()
        urls = {c.url for c in view.children if hasattr(c, "url")}
        assert "https://runwiseai.app/" in urls
        assert "https://x.com/useverseai" in urls
        assert "https://x.com/realthomasgu" in urls

    asyncio.run(check())


def test_string_constants_exist():
    import bot
    assert isinstance(bot.WHAT_IS_VERSE, str) and len(bot.WHAT_IS_VERSE) > 100
    assert isinstance(bot.HOW_TO_CONTRIBUTE, str) and len(bot.HOW_TO_CONTRIBUTE) > 100


def test_commands_registered():
    import bot
    names = {cmd.name for cmd in bot.tree.get_commands()}
    assert "whatisverse" in names
    assert "howtocontribute" in names


def test_whatisverse_contains_key_phrases():
    import bot
    assert "next generation of AI employees" in bot.WHAT_IS_VERSE
    assert "runwiseai.app" in bot.WHAT_IS_VERSE
    assert "🚀 What Makes Verse Different" in bot.WHAT_IS_VERSE
    assert "🧠 What Verse Agents Can Do" in bot.WHAT_IS_VERSE
    assert "🔥 Where We're At" in bot.WHAT_IS_VERSE
    assert "🌎 Our Mission" in bot.WHAT_IS_VERSE


def test_howtocontribute_contains_channels():
    import bot
    assert "<#1507589532512419890>" in bot.HOW_TO_CONTRIBUTE
    assert "<#1507589550904705156>" in bot.HOW_TO_CONTRIBUTE
    assert "<#1507589377486885004>" in bot.HOW_TO_CONTRIBUTE
    assert "<#1507589339373240382>" in bot.HOW_TO_CONTRIBUTE
