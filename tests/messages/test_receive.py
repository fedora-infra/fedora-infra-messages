# Copyright © 2020 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Test fedora_messaging_infragit.messages.receive."""

import pytest
from jsonschema.exceptions import ValidationError

from fedora_messaging_infragit.messages import receive


def test_invalid():
    """
    This tests ensures that the message fails validation.

    The test message here is missing the 'additions' key in the file given in the 'stats' section.
    """
    msg = receive.ReceiveV1(
        body={
            "commit": {
                "agent": "praiskup",
                "branch": "master",
                "email": "praiskup@redhat.com",
                "message": ("copr: builder: put --capability=cap_ipc_lock to site-defaults.cfg\n\n"
                            "It used to be in copr-rpmbuild in mock.cfg.j2 (child.cfg template).  "
                            "But\nthat one shouldn't be overwritten by us.\n"),
                "name": "Pavel Raiskup",
                "path": "/git/ansible",
                "repo": "",
                "rev": "42d5666b3f021503b68febf60595d5000bf929ef",
                "seen": False,
                "stats": {
                    "files": {
                        "roles/copr/backend/files/provision/files/mock/site-defaults.cfg": {
                            "deletions": 0,
                            "lines": 5
                        }
                    },
                    "total": {
                        "additions": 5,
                        "deletions": 0,
                        "files": 1,
                        "lines": 5
                    }
                },
                "summary": "copr: builder: put --capability=cap_ipc_lock to site-defaults.cfg",
                "username": "praiskup"
            }
        }
    )

    with pytest.raises(ValidationError):
        msg.validate()


def test_valid():
    msg = receive.ReceiveV1(
        body={
            "commit": {
                "agent": "praiskup",
                "branch": "master",
                "email": "praiskup@redhat.com",
                "message": ("copr: builder: put --capability=cap_ipc_lock to site-defaults.cfg\n\n"
                            "It used to be in copr-rpmbuild in mock.cfg.j2 (child.cfg template).  "
                            "But\nthat one shouldn't be overwritten by us.\n"),
                "name": "Pavel Raiskup",
                "path": "/git/ansible",
                "repo": "",
                "rev": "42d5666b3f021503b68febf60595d5000bf929ef",
                "seen": False,
                "stats": {
                    "files": {
                        "roles/copr/backend/files/provision/files/mock/site-defaults.cfg": {
                            "additions": 5,
                            "deletions": 0,
                            "lines": 5
                        }
                    },
                    "total": {
                        "additions": 5,
                        "deletions": 0,
                        "files": 1,
                        "lines": 5
                    }
                },
                "summary": "copr: builder: put --capability=cap_ipc_lock to site-defaults.cfg",
                "username": "praiskup"
            }
        }
    )

    msg.validate()
    assert msg.agent == 'praiskup'
    assert msg.branch == 'master'
    assert msg.email == 'praiskup@redhat.com'
    assert msg.message == ("copr: builder: put --capability=cap_ipc_lock to site-defaults.cfg\n\n"
                           "It used to be in copr-rpmbuild in mock.cfg.j2 (child.cfg template).  "
                           "But\nthat one shouldn't be overwritten by us.\n")
    assert msg.name == 'Pavel Raiskup'
    assert msg.path == '/git/ansible'
    assert msg.rev == '42d5666b3f021503b68febf60595d5000bf929ef'
    assert msg.stats == {
        "files": {
            "roles/copr/backend/files/provision/files/mock/site-defaults.cfg": {
                "additions": 5,
                "deletions": 0,
                "lines": 5
            }
        },
        "total": {
            "additions": 5,
            "deletions": 0,
            "files": 1,
            "lines": 5
        }
    }
    assert msg.summary == 'copr: builder: put --capability=cap_ipc_lock to site-defaults.cfg'
    assert msg.username == 'praiskup'
