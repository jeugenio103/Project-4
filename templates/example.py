      <script>
          document.getElementById('form').addEventListener('submit', function(event) {
          event.preventDefault();

          const formData = new FormData(event.target);
          const trackName = formData.get('input');

          fetch('/predict', {
            method: 'POST',
            body: formData
          })
            .then(response => response.text())
            .then(html => {
              const parser = new DOMParser();
              const doc = parser.parseFromString(html, 'text/html');
              const prediction = doc.getElementById('prediction-output').innerHTML;
              document.getElementById('prediction-output').innerHTML = prediction;
            });
        });
        function showPrediction() {
          document.getElementById('prediction-output').style.display = 'block';
        }
      
        function clearFields() {
          document.getElementById('search-input').value = '';
          document.getElementById('prediction-output').innerHTML = '';
          document.getElementById('h4-output').innerHTML = '';
        }
      
        function saveValues() {
          localStorage.setItem('input', document.getElementById('search-input').value);
          localStorage.setItem('prediction', document.getElementById('prediction-output').innerHTML);
        }
      
        function loadValues() {
          document.getElementById('search-input').value = localStorage.getItem('input');
          document.getElementById('prediction-output').innerHTML = localStorage.getItem('prediction');
        }
      
        function savePrediction() {
          localStorage.setItem('prediction', document.getElementById('prediction-output').innerHTML);
        }
      
        function loadPrediction() {
          document.getElementById('prediction-output').innerHTML = localStorage.getItem('prediction');
        }
      
        window.onload = function() {
          clearFields();
          loadPrediction();
          document.getElementById('form').reset();
          document.getElementById('prediction-output').innerHTML = '';
          document.getElementById('h4-output').innerHTML = '';

        }
      
        document.getElementById('form').addEventListener('submit', function(event) {
          showPrediction();
          saveValues();
          savePrediction();
        });
      </script>      
      
      <style>
        #prediction-output {
          font-size: 25px;
          font-weight: bold;
          text-align: center;
          padding-top: 5px;
        }
        .clear-button {
          float: center;
        }
        h4 {
          font-size: 30px;
          font-family: Serif;
          padding-top: 20px;
        }
      </style>

      <div class="container mt-5">
        <div class="row justify-content-center">
          <div class="col-md-6">
            <div style="text-align:center">
              <form id="form" method="post" action="/predict">
                <input type="text" name="input" id="search-input" placeholder="Enter Track Name">
                <input type="submit" value="Predict">
              </form>
              <h4 id="h4-output">{{ input }}</h4>
              <div id="prediction-output">
                Prediction: {{ prediction_string }}
              </div>
            </div>
          </div>
        </div>
      </div>
      <button type="button" class="clear-button" onclick="clearFields()">Clear</button>