from flask import Flask, request, jsonify, render_template, send_file
from text_module import analyze_text, extract_skills
from feedback_module import generate_feedback
from recommendation_module import recommend_improvements
from resume_module import Candidate, build_resume
app = Flask(__name__, template_folder="template")

@app.route("/download_resume")
def download_resume():
    return send_file("resume.txt", as_attachment=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    data = request.json
    name = data.get("name")
    role = data.get("role")
    text = data.get("text")

    analysis = analyze_text(text)
    score, feedback = generate_feedback(analysis)
    skills = extract_skills(text)
    recommendations, learning_links = recommend_improvements(skills, score, feedback)

    candidate = Candidate(name, role, skills, score, feedback, recommendations)
    result = build_resume(candidate)

    return jsonify({
        "score": score,
        "feedback": feedback,
        "skills": skills,
        "recommendations": recommendations,
        "learning_links": learning_links,
        "resume": result
    })

if __name__ == "__main__":
    app.run(debug=True)