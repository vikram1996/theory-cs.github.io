from string import Template
import json
from user_functions import *

template = ["index_template", "feedback_template", "overview_calendar_template", "overview_outcome_template", "overview_application_template", "assignment_template"]
generated = ["index", "feedback", "overview_calendar", "overview_outcome", "overview_application", "assignments"]

for i in range (len(template)):
    substitute_template(template[i], generated[i])