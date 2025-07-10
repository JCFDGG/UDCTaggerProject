import io
import base64
import os
from flask import Flask, render_template, request, url_for
import matplotlib.pyplot as plt
import logging

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()]) # Logs to console

logger = logging.getLogger(__name__)

# Import your models
from models import std_knn, sep_knn, bert, t5  # example models

app = Flask(__name__)

# Route redirects from '/' to default model
@app.route('/')
def index():
    """
    Simple index page. It redirects to any desired model.
    """
    return render_template('index.html')

# Route for model view
@app.route('/<model_name>', methods=['GET', 'POST'])
def model_view(model_name):
    """
    model_name: str
    This function handles the model view for different models.
    It renders a prompt box, a generate button, a text area for output,
    and image if the model generates one.
    """
    prompt = output_text = output_image = None

    # Model routing dictionary
    model_map = {
        'std_knn': std_knn.model,
        'sep_knn': sep_knn.model,
        'bert_classifier': bert.model,
        't5_seq2seq': t5.model}

    model = model_map.get(model_name)
    if model is None:
        logger.error(f"Model '{model_name}' not found. Available models: {list(model_map.keys())}")
        return f"Model '{model_name}' not found", 404

    output_text = "Clique para gerar."  # Default text
    if request.method == 'POST':
        prompt = request.form['prompt']

        # The result has to be given by a predict function
        try:
            result = model.predict(prompt)
        except Exception as e:
            logger.error(f"Error predicting with model {model_name}: {prompt} - {e}")
            result = "Error"
        output_text = result

        # Optional: if model returns a graph
        if hasattr(model, 'plot_output'):  # e.g., defined in model.py
            try:
                fig = model.plot_output(prompt)
                buf = io.BytesIO()
                fig.savefig(buf, format='png')
                buf.seek(0)
                output_image = base64.b64encode(buf.getvalue()).decode('utf8')
                plt.close(fig)
            except Exception as e:
                logger.error(f"Error plotting output for model {model_name}: {prompt} - {e}")
                output_image = None

    return render_template('model.html',
                           model_name=model_name,
                           prompt=prompt,
                           output_text=output_text,
                           output_image=output_image)


@app.route('/sep_knn/mock', methods=['GET', 'POST'])
def mock_view():
    """
    A mock view for the sep_knn model given a standard prompt.
    It's a concept for data drift and performance tracking.
    """
    output_text = None
    prompt = """
    Candle Making Basics: The complete guide to candle making, from equipment and materials to finished product.
    Step-by-step photographs and expert advice guide you through the process, showing you how to avoid common mistakes along the way.
    """



    model = sep_knn.model
    show_full_output = False # Default to not showing full output
    output_text = "Clique para gerar."  # Default text
    if request.method == 'POST':
        prompt = request.form['prompt']

        # The result has to be given by a predict function
        try:
            result = model.predict(prompt)
        except Exception as e:
            logger.error(f"Error predicting with sep_knn model: {prompt} - {e}")
            result = "Error"

        output_text = result
        show_full_output = True
        # Optional: if model returns a graph

    return render_template('mock.html',
                           model_name='Mock Test for sep_knn: Candles',
                           prompt=prompt,
                           output_text=output_text,
                           show_full_output=show_full_output)

if __name__ == '__main__':
    app.run(debug=True)
