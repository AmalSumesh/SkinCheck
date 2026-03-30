import { useState } from "react";
import axios from "axios";

function App() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [explainLoading, setExplainLoading] = useState(false);

  const handleChange = (e) => {
    const file = e.target.files[0];
    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const handleUpload = async () => {
    if (!image) {
      alert("Please select an image first!");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    try {
      setLoading(true);

        const res = await axios.post(
          "https://skin-cancer-classification-gpqz.onrender.com/predict",
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        );

      setResult(res.data);
    }
    catch (error) {
      console.error("Error uploading image:", error);
    }
    finally {
      setLoading(false);
    }
  };

  const handleExplain = async () => {
    if (!image) {
      alert("Please select an image first!");
      return;
    }

    const formData = new FormData();
    formData.append("image", image);

    try {
      setExplainLoading(true);

        const res = await axios.post(
          "https://unspiteful-lukas-unfevered.ngrok-free.dev/explain",
          formData,
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
        );

      setResult((prev) => ({ ...prev, ...res.data }));
    }
    catch (error) {
      console.error("Error fetching explanation:", error);
    }
    finally {
      setExplainLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-black via-gray-900 to-black flex items-center justify-center p-4">
      <div className="max-w-4xl w-full bg-gray-800/50 backdrop-blur-sm rounded-2xl shadow-2xl border border-yellow-500/30 p-10 animate-fade-in">
        <div className="text-center mb-10">
          <h1 className="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-yellow-400 to-yellow-600 mb-4 animate-pulse">
            Skin Cancer Detection
          </h1>
          <p className="text-gray-300 text-lg">Upload an image for AI-powered analysis</p>
        </div>

        {/* Top row: Upload box + Preview box (side by side only when image is selected) */}
        <div className={`grid gap-8 items-stretch mb-8 ${preview ? "md:grid-cols-2" : "grid-cols-1"}`}>
          {/* Upload / Select Image box */}
          <div className="bg-gray-700/50 rounded-xl p-6 border border-yellow-500/20 flex flex-col justify-between min-h-[280px]">
            <div>
              <label className="block text-yellow-400 text-xl font-semibold mb-4 text-center">
                Select an Image
              </label>
              <label className="flex items-center justify-center gap-3 w-full cursor-pointer bg-gray-800 border-2 border-dashed border-yellow-500/50 rounded-lg p-4 hover:border-yellow-400 transition-colors duration-300">
                <input
                  type="file"
                  onChange={handleChange}
                  className="hidden"
                />
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-yellow-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
                </svg>
                <span className={`text-sm font-medium truncate max-w-[220px] ${image ? "text-yellow-400" : "text-gray-400"}`}>
                  {image ? `File chosen: ${image.name}` : "Choose File"}
                </span>
              </label>
            </div>
            <div className="mt-6 flex justify-center">
              <button
                onClick={handleUpload}
                disabled={loading || !image}
                className="w-full bg-gradient-to-r from-yellow-500 to-yellow-600 hover:from-yellow-600 hover:to-yellow-700 text-black font-bold py-4 rounded-xl transition-all duration-300 transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none shadow-lg hover:shadow-yellow-500/25"
              >
                {loading ? (
                  <div className="flex items-center justify-center space-x-2">
                    <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-black"></div>
                    <span>Analyzing...</span>
                  </div>
                ) : (
                  "Predict"
                )}
              </button>
            </div>
          </div>

          {/* Image Preview box — only shown when image is selected */}
          {preview && (
            <div className="bg-gray-700/50 rounded-xl p-6 border border-yellow-500/20 flex flex-col items-center justify-center min-h-[280px]">
              <h3 className="text-2xl text-yellow-400 font-semibold mb-4">Image Preview</h3>
              <img
                src={preview}
                alt="Preview"
                className="max-w-full h-52 md:h-60 rounded-lg border-2 border-yellow-500/50 shadow-lg object-contain"
              />
            </div>
          )}
        </div>

        {/* Prediction box — full width, appears below after predict */}
        {result && (
          <div className="bg-gray-700/50 rounded-xl p-8 border border-yellow-500/20 w-full">
            <h2 className={`text-3xl font-bold text-center mb-6 ${result.prediction.includes("Malignant") ? "text-red-400" : "text-green-400"}`}>
              {result.prediction}
            </h2>

            <div className="text-center mb-6">
              <p className="text-yellow-400 text-lg mb-2">Confidence Level</p>
              <div className="w-full bg-gray-600 rounded-full h-4 mb-2">
                <div
                  className="bg-gradient-to-r from-yellow-500 to-yellow-600 h-4 rounded-full transition-all duration-1000"
                  style={{ width: `${result.confidence * 100}%` }}
                ></div>
              </div>
              <p className="text-gray-300 font-semibold">{(result.confidence * 100).toFixed(2)}%</p>
            </div>

            <div className="text-center mb-6">
              <button
                onClick={handleExplain}
                disabled={explainLoading}
                className="bg-yellow-500 hover:bg-yellow-600 text-black font-semibold py-2 px-5 rounded-lg transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {explainLoading ? "Explaining..." : "Explain"}
              </button>
            </div>

            {result.explanation && (
              <div className="bg-gray-800/60 border border-yellow-500/20 rounded-xl px-6 py-5 mb-6">
                <div className="flex items-center gap-2 mb-3">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 text-yellow-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
                  </svg>
                  <h4 className="text-yellow-400 font-semibold text-base tracking-wide">AI Explanation</h4>
                </div>
                <p className="text-gray-300 text-sm leading-relaxed">{result.explanation}</p>
              </div>
            )}

            {result.gradcam && (
              <div>
                <h3 className="text-2xl text-yellow-400 font-semibold text-center mb-4">Grad-CAM Visualization</h3>
                <div className="flex justify-center">
                  <img
                    src={`data:image/jpeg;base64,${result.gradcam}`}
                    alt="Grad-CAM"
                    className="max-w-full h-60 md:h-72 rounded-lg border-2 border-yellow-500/50 shadow-lg object-contain"
                  />
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
