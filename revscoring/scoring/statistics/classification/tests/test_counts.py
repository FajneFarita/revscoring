import json
import pickle

from nose.tools import eq_

from ..counts import Counts


def test_counts():
    c = Counts(
        [True, False],
        [({'prediction': True}, True)] * 10 +
        [({'prediction': True}, False)] * 20 +
        [({'prediction': False}, False)] * 30 +
        [({'prediction': False}, True)] * 40,
        'prediction'
    )

    print(c.format_str({}))
    print(json.dumps(c.format_json({}), indent=2))
    eq_(c.lookup("n"), 100)
    eq_(c.lookup("labels.true"), 50)
    eq_(c.lookup("predictions.false.false"), 30)

    pickle.loads(pickle.dumps(c))
