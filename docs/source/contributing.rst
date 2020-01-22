============
Contributing
============

This page contains information about contributing to this project.


Contribution guidelines
=======================

Before you submit a pull request, please ensure that it meets these criteria:

* All tests must pass.
* Code must have 100% test coverage.
* Functions, methods, and classes must have docblocks that explain what the code block is, and
  describing any parameters it accepts and what it returns (if anything).
* Parameter and return value types should be declared using `type hints`_.
* Code must follow `PEP-8 <https://www.python.org/dev/peps/pep-0008/>`_.
* Make sure your commits are atomic. With only rare exceptions, each improvement or bug fix should
  have exactly one commit. This makes it much easier to peruse the git history to find out which
  changes relate to a feature or bugfix implementation, and is particularly valuable when commits
  need to be cherry picked. If you need to build upon prior unmerged commits while fixing a
  different issue, feel free to send more than one commit in the same pull request.
* Your commit messages must include a Signed-off-by tag with your name and e-mail address,
  indicating that you agree to the
  `Developer Certificate of Origin <https://developercertificate.org/>`_, which reads::

   Developer Certificate of Origin
   Version 1.1

    Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
    1 Letterman Drive
    Suite D4700
    San Francisco, CA, 94129

    Everyone is permitted to copy and distribute verbatim copies of this
    license document, but changing it is not allowed.


    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.

  For example, Randy Barlow's commit messages include this line::

   Signed-off-by: Randy Barlow <randy@electronsweatshop.com>
* Code may be submitted by opening a pull request at
  `github.com/fedora-infra/fedora-messaging-infragit <https://github.com/fedora-infra/fedora-messaging-infragit/>`_.


Development tooling
===================

The project includes some scripts in the ``devel/`` folder that are handy for development.
You will need to install `podman`_ on your system to use these. ``build.sh`` builds a container that
has the necessary dependencies. ``tox.sh`` is a handy script that runs `tox`_ in that container for
you. ``tox.sh`` accepts the same parameters as tox. You can run the tests using tox with no
parameters.

If you prefer not to use podman, you can also install tox on your system and use it directly.


.. _type hints: https://docs.python.org/3/library/typing.html
.. _podman: https://podman.io/
.. _tox: https://tox.readthedocs.io/en/latest/
