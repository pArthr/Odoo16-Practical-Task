# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.service import common
from odoo.exceptions import ValidationError

from . import models

def pre_init_check(cr):
    version_info = common.exp_version()#func use for checking version of odoo
    server_serie =version_info.get('server_serie')
    if server_serie!='16.0':
        raise ValidationError('Module support Odoo series 16.0. Your Odoo series is {}.'.format(server_serie))
    return True
