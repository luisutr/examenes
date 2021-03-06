import pytest

SAMPLES = [
    [1, [2, 3], [4, 5], [[1]]],
    [1, 2, 3, 4, []],
    [[], [], [], []],
    [[[2, 3, 4], [1, 2], 2, [1]], [2, [2, 3], 1, 4, [2, 2, 6, 7]], 5]
]

ANSWERS = [
    [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[2, 2, 2, 2], [3, 3, 3, 3], [0, 0, 0, 0], [0, 0, 0, 0]], [[4, 4, 4, 4], [5, 5, 5, 5], [0, 0, 0, 0], [0, 0, 0, 0]], [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]],
    [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [0, 0, 0, 0, 0]],
    [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
    [[[2, 3, 4, 0, 0], [1, 2, 0, 0, 0], [2, 2, 2, 2, 2], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[2, 2, 2, 2, 2], [2, 3, 0, 0, 0], [1, 1, 1, 1, 1], [4, 4, 4, 4, 4], [2, 2, 6, 7, 0]], [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]]
]

ANSWERS_WITH_DEFAULT = [
    [[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], [[2, 2, 2, 2], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]], [[4, 4, 4, 4], [5, 5, 5, 5], [3, 3, 3, 3], [3, 3, 3, 3]], [[1, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]]],
    [[1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4], [3, 3, 3, 3, 3]],
    [[3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3], [3, 3, 3, 3]],
    [[[2, 3, 4, 3, 3], [1, 2, 3, 3, 3], [2, 2, 2, 2, 2], [1, 3, 3, 3, 3], [3, 3, 3, 3, 3]], [[2, 2, 2, 2, 2], [2, 3, 3, 3, 3], [1, 1, 1, 1, 1], [4, 4, 4, 4, 4], [2, 2, 6, 7, 3]], [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3]], [[3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3], [3, 3, 3, 3, 3]]]
]

def test_normalize():
    from exam import normalize
    for t,ans,ans_def in zip(SAMPLES, ANSWERS, ANSWERS_WITH_DEFAULT):
        assert normalize(t) == ans
        assert normalize(t, 3) == ans_def


def test_sol_equa():
    from exam import sol_equa
    assert list(sol_equa(12)) == [(4, 1)]
    assert list(sol_equa(13)) == [(7, 3)] 
    assert list(sol_equa(16)) == [(4, 0)]
    assert list(sol_equa(17)) == [(9, 4)]
    assert list(sol_equa(90005)) == [(45003, 22501), (9003, 4499), (981, 467), (309, 37)]
    assert list(sol_equa(90002)) == []

def test_int2ip():
    from exam import decode_tcp
    assert decode_tcp(76546546547654765476547654765476542136762123434343) == {
        'ack_nr': 3246118151,
        'checksum': 24593,
        'dst_port': 52764,
        'recv_wnd': 20030,
        'seq_nr': 2409937118,
        'src_port': 14695
    }
    assert decode_tcp(16431264643232115432323334354375437543475647657898765765754343) == {
        'ack_nr': 176312414,
        'checksum': 52819,
        'dst_port': 32574,
        'recv_wnd': 54017,
        'seq_nr': 4007708153,
        'src_port': 48615
    }
    assert decode_tcp(132122212123335454544322211212122222376767777662212111111) == {
        'ack_nr': 2904142787,
        'checksum': 756,
        'dst_port': 51777,
        'recv_wnd': 24230,
        'seq_nr': 1308022401,
        'src_port': 64263
    }
