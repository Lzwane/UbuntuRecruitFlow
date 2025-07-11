import cohere
import re

COHERE_API_KEY = "COHERE_API_KEY"  #create a cohere account and use the api key

co = cohere.Client(COHERE_API_KEY)

def generate_job_description(data: dict) -> str:
    """
    Generate a concise job description from structured job data using Cohere.

    data: dictionary that contains job information, e.g. role_summary, responsibilities, skills, experience
    """

    prompt = f"""
    You are an AI assistant helping recruiters write compelling job descriptions.

    Based on the information below, generate a clear, professional, and concise job description suitable for a job posting. Include an engaging introduction that naturally mentions the job title, location, and work type. Structure the output into sections with responsibilities and skills. Avoid repeating field labels.

    ---

    Job Title: {data.get('job_title')}
    Location: {data.get('location')}
    Work Type: {data.get('work_type')}
    Role Summary: {data.get('role_summary')}
    Key Responsibilities: {', '.join(data.get('key_responsibilities', []))}
    Required Skills: {', '.join(data.get('required_skills', []))}
    Preferred Skills: {', '.join(data.get('preferred_skills', [])) if data.get('preferred_skills') else 'None'}
    Experience: {data.get('min_experience_years')} to {data.get('max_experience_years')} years

    ---

    Job Description:
    """


    response = co.generate(
        model="command-r-plus-08-2024",
        prompt=prompt,
        max_tokens=500,
        temperature=0.7,
        k=0,
        stop_sequences=["--END--"],
    )

    generated_text = response.generations[0].text.strip()
    return generated_text

def extract_score(text: str) -> int:
    """
    Extracts the score from the AI response text.
    Expected format in text: 'Score: <number>'
    Returns an int score between 0 and 100. Returns 0 if no valid score found.
    """
    match = re.search(r"Score:\s*(\d{1,3})", text)
    if match:
        score = int(match.group(1))
        # Clamp score between 0 and 100
        return max(0, min(score, 100))
    return 0

def extract_feedback(text: str) -> str:
    """
    Extracts the feedback text from the AI response.
    Expected format in text: 'Feedback: <feedback text>'
    Returns the feedback string or a default message if not found.
    """
    match = re.search(r"Feedback:\s*(.+)", text, re.DOTALL)
    if match:
        # Striping any trailing whitespace/newlines
        feedback = match.group(1).strip()
        return feedback
    return "No feedback provided."


def analyze_cv_match(cv_data: dict, job_description: str) -> dict:
    skills = ', '.join(cv_data.get('skills', [])) or 'N/A'
    projects = ', '.join(cv_data.get('projects', [])) or 'N/A'
    experience = ', '.join(
        [f"{x.get('position', 'Unknown')} at {x.get('company_name', 'Unknown')}" for x in cv_data.get('experience', [])]
    ) or 'N/A'
    education = ', '.join(
        [f"{x.get('qualification', 'Unknown')} at {x.get('institution', 'Unknown')}" for x in cv_data.get('education', [])]
    ) or 'N/A'

    prompt = f"""
Compare the following job description and CV.
Rate the match from 0 to 100 as "Score: <number>" on one line.
Then provide 2-3 sentences of feedback starting with "Feedback:".

Job Description:
{job_description}

CV Summary:
Name: {cv_data.get('name', '')} {cv_data.get('surname', '')}
Skills: {skills}
Projects: {projects}
Experience: {experience}
Education: {education}
"""

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=300,
            temperature=0.6
        )
        text = response.generations[0].text.strip()
    except Exception as e:
        return {"rating": 0, "feedback": f"Error analyzing CV: {str(e)}"}

    rating = extract_score(text)  # gets the score
    feedback = extract_feedback(text)  # gets the feedback

    return {
        "rating": rating,
        "feedback": feedback
    }

