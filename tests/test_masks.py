import pytest

from scr.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("number, result", [("124587", None), ("", None), ("7001555521219784", "7001 55** **** 9784")])
def test_masks_card(number, result):
    assert get_mask_card_number(number) == result


@pytest.mark.parametrize("number, result", [("124587", None), ("", None), ("70015555212197841414", "**1414")])
def test_masks_account(number, result):
    assert get_mask_account(number) == result
