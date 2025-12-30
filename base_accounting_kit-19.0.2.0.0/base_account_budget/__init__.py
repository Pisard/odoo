# -*- coding: utf-8 -*-

from . import models


def enable_analytic_accounting(env):
    group = env.ref('analytic.group_analytic_accounting')
    if group:
        users = env['res.users'].search([('share', '=', False)])
        for user in users:
            user.write({'group_ids': [(4, group.id)]})
