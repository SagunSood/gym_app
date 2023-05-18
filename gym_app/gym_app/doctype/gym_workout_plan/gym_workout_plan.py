# Copyright (c) 2022, Sagun and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class GymWorkoutPlan(WebsiteGenerator):
	# set the route for the workout plan
	def before_save(self):
		if not self.route:
			self.route = f"/{self.name}"
