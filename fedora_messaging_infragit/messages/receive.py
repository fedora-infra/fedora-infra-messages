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
"""Define message schemas for commit messages to the Fedora infrastructure git repository."""

from fedora_messaging import message


SCHEMA_URL = 'https://fedora-messaging-infragit.readthedocs.io/en/latest/_schema'


class ReceiveV1(message.Message):
    """This message is sent when a commit is pushed to the Fedora Infrastructure git repository."""

    topic = "infragit.receive"

    body_schema = {
        '$id': f'{SCHEMA_URL}/v1/{topic}#',
        '$schema': 'https://json-schema.org/draft/2019-09/schema',
        'description': 'A commit was pushed to the infra git repository',
        'type': 'object',
        'properties': {
            'commit': {
                'type': 'object',
                'description': 'A git commit',
                'properties': {
                    'agent': {
                        'type': 'string',
                        'description': 'The FAS account that pushed the commit',
                    },
                    'branch': {
                        'type': 'string',
                        'description': 'The branch the commit was pushed to',
                    },
                    'email': {
                        'type': 'string',
                        'description': 'The e-mail address of the commit author',
                    },
                    'message': {
                        'type': 'string',
                        'description': 'The full commit message',
                    },
                    'name': {
                        'type': 'string',
                        'description': 'The name of the commit author',
                    },
                    'path': {
                        'type': 'string',
                        'description': 'The path to the git repository',
                    },
                    'rev': {
                        'type': 'string',
                        'description': 'The commit hash',
                    },
                    'stats': {
                        'type': 'object',
                        'description': 'Statistics about the changes made in the commit',
                        'properties': {
                            'files': {
                                'type': 'object',
                                'description': 'Maps paths to change statistics',
                                'patternProperties': {
                                    '.*': {
                                        'type': 'object',
                                        'description': 'Change statistics for given path',
                                        'properties': {
                                            'additions': {
                                                'type': 'integer',
                                                'description': 'The number of lines added'
                                            },
                                            'deletions': {
                                                'type': 'integer',
                                                'description': 'The number of lines removed'
                                            },
                                            'lines': {
                                                'type': 'integer',
                                                'description': 'The number of lines altered'
                                            },
                                        },
                                        'required': ['additions', 'deletions', 'lines']
                                    }
                                }
                            },
                            'total': {
                                'type': 'object',
                                'description': 'Change statistics for all paths',
                                'properties': {
                                    'additions': {
                                        'type': 'integer',
                                        'description': 'The number of lines added'
                                    },
                                    'deletions': {
                                        'type': 'integer',
                                        'description': 'The number of lines removed'
                                    },
                                    'files': {
                                        'type': 'integer',
                                        'description': 'The number of files altered'
                                    },
                                    'lines': {
                                        'type': 'integer',
                                        'description': 'The number of lines altered'
                                    },
                                },
                                'required': ['additions', 'deletions', 'files', 'lines']
                            }
                        },
                        'required': ['files', 'total']
                    },
                    'summary': {
                        'type': 'string',
                        'description': 'The first line of the commit message',
                    },
                    'username': {
                        'type': 'string',
                        'description': 'The FAS account that pushed the commit',
                    },
                },
                'required': ['agent', 'branch', 'email', 'message', 'name', 'path', 'rev', 'stats',
                             'summary', 'username'],
            }
        },
        'required': ['commit'],
    }

    @property
    def agent(self) -> str:
        """Return the user who pushed the commit to the repository."""
        return self.body['commit']['agent']

    @property
    def branch(self) -> str:
        """Return the branch that the commit was pushed into."""
        return self.body['commit']['branch']

    @property
    def email(self) -> str:
        """Return the e-mail address of the commit author."""
        return self.body['commit']['email']

    @property
    def message(self) -> str:
        """Return the full commit message."""
        return self.body['commit']['message']

    @property
    def name(self) -> str:
        """Return the name of the commit author."""
        return self.body['commit']['name']

    @property
    def path(self) -> str:
        """Return the path to the git repo."""
        return self.body['commit']['path']

    @property
    def rev(self) -> str:
        """Return the git commit id."""
        return self.body['commit']['rev']

    @property
    def stats(self) -> dict:
        """
        Return a dictionary describing the statistics for changes in the commit.

        The dictionary has two keys: 'files' and 'total'.

        'files' indexes another dictionary, whose keys are paths, and each key indexes a dictionary
        with keys 'additions', 'deletions', and 'lines'. These in turn index integers that indicate
        how many additions and deletions were made to the given path, and the total number of lines
        altered for the given path.

        'total' indexes a dictionary with keys 'additons', 'deletions', 'files', and 'lines', each
        of which index an integer describing the total number of additions, deletions, files
        altered, and lines altered in the commit.
        """
        return self.body['commit']['stats']

    @property
    def summary(self) -> str:
        """Return the first line of the commit message."""
        return self.body['commit']['summary']

    @property
    def username(self) -> str:
        """Return the user who pushed the commit to the repository."""
        return self.body['commit']['username']
