from typing import Any

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_with_EXECUTED(test_processing_list: Any) -> None:
    assert filter_by_state(test_processing_list) == \
           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]


def test_filter_by_state_with_CANCELED(test_processing_list: Any) -> None:
    assert filter_by_state(test_processing_list, 'CANCELED') == \
           [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


@pytest.mark.parametrize('state, expected',
                         [('EXECUTED',
                           [
                               {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                               {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ('CANCELED',
                           [
                               {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                               {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])])
def test_filter_by_state(test_processing_list: Any, state: Any, expected: Any) -> None:
    assert filter_by_state(test_processing_list, state) == expected


def test_filter_by_state_with_wrong_state(test_processing_list: Any) -> None:
    with pytest.raises(ValueError):
        filter_by_state(test_processing_list, 'WRONG_STATE')


def test_sort_by_date_decreasing(test_processing_list: Any) -> None:
    assert sort_by_date(test_processing_list) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_sort_by_date_increasing(test_processing_list: Any) -> None:
    assert sort_by_date(test_processing_list, False) == [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}
    ]


@pytest.mark.parametrize('decreasing, expected',
                         [(True,
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          (False,
                           [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}])])
def test_sort_by_date(test_processing_list: Any, decreasing: Any, expected: Any) -> None:
    assert sort_by_date(test_processing_list, decreasing) == expected


@pytest.mark.parametrize('decreasing, expected',
                         [(False,
                           [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 615064592, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]),
                          (True,
                           [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                            {'id': 615064592, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
                            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])])
def test_sort_by_same_date(test_processing_list_same_data: Any, decreasing: Any, expected: Any) -> None:
    assert sort_by_date(test_processing_list_same_data, decreasing) == expected


@pytest.mark.parametrize('wrong_operation', [
    ({'id': 596226727, 'state': 'CANCELED', 'date': 'aaaa-09-12T21:27:25.241689'}),
    ({'id': 625064591, 'state': 'CANCELED', 'date': '2018-aa-14T08:21:33.419441'}),
    ({'id': 616064592, 'state': 'CANCELED', 'date': '2018-10-aaT08:21:33.419441'}),
    ({'id': 615664592, 'state': 'CANCELED', 'date': '2018-99-14T08:21:33.419441'}),
    ({'id': 615074592, 'state': 'CANCELED', 'date': '2018-10-99T08:21:33.419441'})])
def test_sort_by_wrong_date(test_processing_list: Any, wrong_operation: Any) -> None:
    test_wrong_processing_list = test_processing_list[::]
    test_wrong_processing_list.append(wrong_operation)
    with pytest.raises(ValueError):
        sort_by_date(test_wrong_processing_list)
