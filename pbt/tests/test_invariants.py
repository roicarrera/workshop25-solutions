from hypothesis import given, strategies as st
from Task5.invariants import reverse, sort, deduplicate

@given(st.lists(st.integers()))
def test_reverse_preserves_length(xs):
    assert len(reverse(xs)) == len(xs)

@given(st.lists(st.integers()))
def test_reverse_twice_returns_input(xs):
    assert reverse(reverse(xs)) == xs

@given(st.lists(st.integers()))
def test_reverse_first_was_last_in_input(xs):
    assert reverse(xs)[0:1] == xs[-1:]


@given(st.lists(st.integers()))
def test_sort_preserves_multiset(xs):
    assert set(sort(xs)) == set(xs)

@given(st.lists(st.integers()))
def test_sort_is_idempotent(xs):
    assert sort(sort(xs)) == sort(xs)

@given(st.lists(st.integers()))
def test_sort_preserves_length(xs):
    assert len(sort(xs)) == len(xs)


@given(st.lists(st.integers()))
def test_deduplicate_output_is_unique(xs):
    output = deduplicate(xs)
    assert len(set(output)) == len(output)

@given(st.lists(st.integers()))
def test_deduplicate_output_is_subset_of_input(xs):
    assert set(deduplicate(xs)).issubset(set(xs))

@given(st.lists(st.integers()))
def test_deduplicate_length_is_less_or_equal(xs):
    assert len(deduplicate(xs)) <= len(xs)
