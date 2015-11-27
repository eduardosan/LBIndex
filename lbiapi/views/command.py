#!/bin/env python
# -*- coding: utf-8 -*-

from . import CustomView


class CommandView(CustomView):
    """??????????????????????????????"""

    def __init__(self, context, request):
        super(CommandView, self).__init__(context, request)

    def post_command(self):
        """??????????????????????????????"""

        params, method = self.split_req(self.request)


        print("> ------------------------------------------------------------")
        print(str(params))
        print(str(method))
        print("< ------------------------------------------------------------")


        rtn_vals = self.context.post_command(params)
        self.rtn_vals.append(rtn_vals)
        return self.cmd_resp()
        # return self.context.post_command()

    def get_command(self):
        """??????????????????????????????"""

        rtn_vals = self.context.get_command()
        self.rtn_vals.append(rtn_vals)
        return self.cmd_resp()

    def put_command(self):
        """??????????????????????????????"""

        return self.context.put_command()

    def delete_command(self):
        """??????????????????????????????"""

        return self.context.delete_command()
