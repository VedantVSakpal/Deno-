class DenoBot:
    def __init__(self):
        self.name = "Deno"

    def respond(self, user_input: str) -> str:
        text = (user_input or "").strip().lower()

        if not text:
            return f"Hello! I am {self.name}, your college assistant. How can I help you today?"

        greetings = [
            "hello", "hi", "hey", "good morning", "good afternoon", "good evening", "good night"
        ]
        if any(word in text for word in greetings):
            return f"Hello! I am {self.name}, your college assistant. I can help with college details, fees, courses, campus information, events, social media, and maps."

        if any(word in text for word in ["what is the name of college", "name of college", "college name", "what is the college name", "which college"]):
            return "The college name is Parul University."

        if any(word in text for word in ["where is the college located", "where is the college", "location of college", "college location", "located in", "city"]):
            return "Parul University is located in Vadodara, Gujarat."

        if any(word in text for word in ["what is parul university", "parul university", "about parul university", "tell me about parul university"]):
            return "Parul University is a reputed university in Vadodara, Gujarat, known for its academic programs, campus facilities, and student support services."

        if any(word in text for word in ["fee", "fees", "payment"]):
            return "Parul University has different fee structures based on the course, program, and admission type. You can ask me about a specific course for more details."

        if any(word in text for word in ["course", "courses", "department", "departments"]):
            return "Parul University offers many programs in engineering, management, medicine, law, pharmacy, design, and more. I can help you learn about a specific course."

        if any(word in text for word in ["campus", "building", "block", "lab", "library", "hostel"]):
            return "The campus includes academic buildings, laboratories, libraries, hostels, cafeterias, sports facilities, and administration offices."

        if any(word in text for word in ["event", "events", "festival", "workshop"]):
            return "Parul University hosts cultural festivals, technical events, workshops, seminars, and sports activities throughout the year."

        if any(word in text for word in ["social media", "instagram", "linkedin", "whatsapp", "twitter", "x.com"]):
            return "You can follow Parul University on Instagram, LinkedIn, WhatsApp updates, and Twitter/X for announcements and events."

        if any(word in text for word in ["owner", "president", "vice president", "hod", "dean", "principal"]):
            return "For leadership and administrative contact details, you can check the official university website or contact the administration office."

        if any(word in text for word in ["map", "location", "navigate", "direction", "route"]):
            return "I can help guide you to classrooms, departments, labs, hostels, and important facilities using the campus map."

        if any(word in text for word in ["admission", "enquiry", "apply"]):
            return "For admission help, you can ask about eligibility, required documents, deadlines, and fee guidance."

        if any(word in text for word in ["document", "documents", "deadline", "deadlines", "eligibility", "certificate"]):
            return "Admission documents usually include ID proof, academic certificates, passport-size photos, and other program-specific documents. Please check the official admission portal for the latest requirements."

        if any(word in text for word in ["help", "support", "what can you do"]):
            return "I can answer questions about college details, fees, courses, campus information, events, social media, leadership information, and maps."

        return "I can help with college details, fees, courses, campus information, events, social media, leadership information, and maps. Ask me anything about Parul University."
