import os
    
def generate_invitations(template, attendees):    
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(att, dict) for att in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        output = template
        output = output.replace("{name}", attendee.get("name", "N/A"))
        output = output.replace("{event_title}", attendee.get("event_title", "N/A"))
        output = output.replace("{event_date}", attendee.get("event_date", "N/A") or "N/A")
        output = output.replace("{event_location}", attendee.get("event_location", "N/A"))
        
        output_filename = f"output_{index}.txt"
        with open(output_filename, 'w') as file:
            file.write(output)
        print(f"Generated {output_filename}")

template_content = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team"""
my_attendees = [
    {"name": "Liam", "event_title": "Python Conference", "event_date": "2024-07-15", "event_location": "San Juan"},
    {"name": "Ricky", "event_title": "Data Science Workshop", "event_date": "2024-08-20", "event_location": "Ponce"},
    {"name": "Ryan", "event_title": "AI Summit", "event_date": None, "event_location": "Rio Grande"}
]

generate_invitations(template_content, attendees)
