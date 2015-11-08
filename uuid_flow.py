# encoding: utf-8

import sys
import uuid
from workflow import Workflow

def main(wf):
    val = "%s" % uuid.uuid4()
    wf.add_item(title=val, valid=True, arg = val)
    wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow(update_settings={'version': 'v0.1', 'github_slug': 'cholick/uuid_alfred_flow'})
    sys.exit(wf.run(main))
