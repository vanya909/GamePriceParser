from site_parsers import zaka_zaka_parser, steambuy_parser, steampay_parser, GameNotFoundError


parsers = [
    zaka_zaka_parser,
]


def _get_parser_name(parser):
    return parser.__name__.replace('_', ' ').title()


def parse(game_title):
    for site_parser in parsers:
        try:
            name, price = site_parser(game_title=game_title)
            print(f'{_get_parser_name(site_parser)} - {name}, {price}p')
        except GameNotFoundError as gnfe:
            print(_get_parser_name(site_parser), '-', gnfe)

