import gradio as gr
from file_parser import extract_text
from rag_pipeline import store_resume, retrieve_chunks
from ranking import score_resume


def process(jd_file, resume_files):
    try:
        jd_text = extract_text(jd_file)

        results = []

        for file in resume_files:
            resume_text = extract_text(file)

            store_resume(resume_text, file.name)

            relevant_chunks = retrieve_chunks(jd_text)

            analysis = score_resume(jd_text, relevant_chunks)

            results.append({
                "resume": file.name,
                "analysis": analysis
            })

        output_text = ""

        for r in results:
            output_text += f"\n📄 Resume: {r['resume']}\n"
            output_text += f"Score: {r['analysis']['score']}\n"
            output_text += f"Status: {r['analysis']['status']}\n"

        return output_text

    except Exception as e:
        return f"ERROR: {str(e)}"


with gr.Blocks() as app:
    gr.Markdown("# 🤖 AI Resume Screening Assistant")

    jd_input = gr.File(label="Upload Job Description")
    resume_input = gr.File(file_count="multiple", label="Upload Resumes")

    output = gr.Textbox(label="Results", lines=20)

    submit = gr.Button("Analyze")

    submit.click(process, inputs=[jd_input, resume_input], outputs=output)

app.launch()