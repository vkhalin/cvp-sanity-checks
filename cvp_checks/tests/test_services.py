import pytest
import json
import os
from cvp_checks import utils


@pytest.mark.parametrize(
    "group",
    utils.get_groups(os.path.basename(__file__))
)
def test_check_services(local_salt_client, group):
    if "skipped" in group:
        pytest.skip("skipped in config")
    output = local_salt_client.cmd(group, 'service.get_all', expr_form='pcre')

    if len(output.keys()) < 2:
        pytest.skip("Nothing to compare - only 1 node")

    nodes = []
    pkts_data = []
    my_set = set()

    for node in output:
        nodes.append(node)
        my_set.update(output[node])

    for srv in my_set:
        diff = []
        row = []
        for node in nodes:
            if srv in output[node]:
                diff.append(srv)
                row.append("{}: +".format(node))
            else:
                row.append("{}: No service".format(node))
        if diff.count(diff[0]) < len(nodes):
            row.sort()
            row.insert(0, srv)
            pkts_data.append(row)
    assert len(pkts_data) <= 1, \
        "Several problems found for {0} group: {1}".format(
        group, json.dumps(pkts_data, indent=4))
