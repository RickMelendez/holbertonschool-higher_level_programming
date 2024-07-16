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
        output_filename = f"output_{index}.txt"
        
        invitation_text = template.format(
            name=attendee.get('name', 'N/A'),
            event_title=attendee.get('event_title', 'N/A'),
            event_date=attendee.get('event_date', 'N/A'),
            event_location=attendee.get('event_location', 'N/A')
        )
