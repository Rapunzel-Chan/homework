import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize('state, expected', [('EXECUTED', [{'id': 41428829, 'state': 'EXECUTED',
                                                            'date': '2019-07-03T18:35:29.512364'},
                                                           {'id': 939719570, 'state': 'EXECUTED',
                                                            'date': '2018-06-30T02:08:58.425572'}]),
                                             ('CANCELED', [{'id': 594226727, 'state': 'CANCELED',
                                                            'date': '2018-09-12T21:27:25.241689'},
                                                           {'id': 615064591, 'state': 'CANCELED',
                                                            'date': '2018-10-14T08:21:33.419441'}])])
def test_filter_by_state(data, state, expected) -> None:
    assert filter_by_state(data, state) == expected


def test_filter_by_state_missing(data) -> None:
    with pytest.raises(KeyError):
        filter_by_state(data, state='123')


def test_sort_by_date(data) -> None:
    assert sort_by_date(data, reverse=False)
    assert sort_by_date(data, reverse=True)
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED',
                          'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED',
                          'date': '2019-07-03T18:35:29.512364'},
                         {'id': 594226727, 'state': 'CANCELED',
                          'date': '2019-07-03T18:35:29.512364'}])


def test_sort_by_date_wrong_format(data) -> None:
    with pytest.raises(ValueError):
        sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33T.'}
                      ])
