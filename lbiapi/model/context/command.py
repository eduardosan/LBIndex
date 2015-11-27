#!/bin/env python
# -*- coding: utf-8 -*-

import subprocess
from pyramid.renderers import render_to_response

from ..LbIndex import LbIndex


class CommandFactory():
    """??????????????????????????????"""

    def __init__(self, request):
        self.request = request
        self.lb_index = LbIndex(request)
        pass

    def post_command(self, params):
        """??????????????????????????????"""

        param_direct = params.get("directive", None)
        post_cmd_out = None
# usage: lbindex <start>                     Start the service
# or: lbindex <stop>                      Stop the service
# or: lbindex <restart>                   Restart the service
# or: lbindex <status>                    Get service status
# or: lbindex <index>                     Index/reindex indexable bases
# or: lbindex <cmd -a <value>>            Pass specific commands

        if param_direct == "start":
            print("start")
            post_cmd_out = self.lb_index.start()
        elif param_direct == "stop":
            print("stop")
            post_cmd_out = self.lb_index.stop()
        elif param_direct == "restart":
            print("restart")
        elif param_direct == "status":
            print("status")
        elif param_direct == "index":
            print("index")
        elif param_direct == "cmd":
            print("cmd")
            if params.get("action", None):
                print(params["action"])
                pass
            else:
                print("Falta o parâmetro \"action\"!")
        else:
            print("Falta o parâmetro \"directive\"!")

        # popen_out = subprocess.Popen(
            # "cd /usr/local/lbneo/virtenvlb2.6/src/"\
            # "LBIndex && /usr/local/lbneo/virtenvlb2.6/bin/python "\
            # "lbindex stop", 
            # shell=True, 
            # stdout=subprocess.PIPE, 
            # stderr=subprocess.PIPE)
        # out, err = popen_out.communicate()

        # output = ""
        # if out:
            # output = out
        # if err:
            # output = output + err


        # TODO: Tratar esse retorno! By Questor
        return post_cmd_out

        # # print("post_command")
        # renderer = "../../templates/mytemplate.pt"
        # return render_to_response(
            # renderer, 
            # {'project': 'LBIApi'}, 
            # request=self.request)

    def get_command(self):
        """??????????????????????????????"""

        # print("get_command")
        popen_out = subprocess.Popen(
            "cd /usr/local/lbneo/virtenvlb2.6/src/"\
            "LBIndex && /usr/local/lbneo/virtenvlb2.6/bin/python "\
            "lbindex stop", 
            shell=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE)
        out, err = popen_out.communicate()

        output = ""
        if out:
            output = out
        if err:
            output = output + err

        return output

    def put_command(self):
        """??????????????????????????????"""

        # print("put_command")
        renderer = "../../templates/mytemplate.pt"
        return render_to_response(
            renderer, 
            {'project': 'LBIApi'}, 
            request=self.request)

    def delete_command(self):
        """??????????????????????????????"""

        # print("delete_command")
        renderer = "../../templates/mytemplate.pt"
        return render_to_response(
            renderer, 
            {'project': 'LBIApi'}, 
            request=self.request)