# Copyright (c) 2022, Sagun and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class ClassBooking(WebsiteGenerator):
	def before_save(self):
		if not self.route:
			self.route = f"/{self.name}"
