from odoo import models, fields, api

class AssetHistory(models.Model):
    _name = 'asset.history'
    _description = "Asset Usage History"

    asset_id = fields.Many2one("account.asset.asset", string="Asset", required=True, ondelete="cascade")
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)
    location = fields.Char(string="Location")  
    start_date = fields.Date(string="Start Date", default=fields.Date.today)
    end_date = fields.Date(string="End Date")
    note = fields.Text(string="Notes")
    
    @api.model
    def create(self, vals):
        # Cari histori penggunaan terakhir dari asset yang sama
        last_history = self.search([
            ('asset_id', '=', vals.get('asset_id'))
        ], order='start_date desc', limit=1)
        
        # Jika ada histori sebelumnya, update end_date dengan start_date yang baru
        if last_history:
            last_history.end_date = vals.get('start_date')
        
        return super(AssetHistory, self).create(vals)

class AccountAsset(models.Model):
    _inherit = 'account.asset.asset'

    usage_history_ids = fields.One2many("asset.history", "asset_id", string="Usage History")