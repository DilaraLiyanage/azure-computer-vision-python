# 🧠 Azure Computer Vision Project

This project demonstrates how to use the **Azure Computer Vision API** with **Python** to analyze images and extract meaningful insights. It features modular input via **JSON**, robust error handling, and clean integration with Azure services.

This project was built as part of a **Coursera course** and reflects the **practical application** of cloud-based computer vision.

---

## 📂 Project Structure

```yaml
ComputerVisionProject/
├── vision_test.py       # Main Python script
├── image.json           # JSON input with image URLs or paths
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not uploaded)
├── .gitignore           # Files to exclude from Git
├── LICENSE              # MIT license (optional)
└── README.md            # Project overview and instructions
```

---

## 🚀 Getting Started

### **1. Clone the Repository**

```bash
git clone https://github.com/your-username/ComputerVisionProject.git
cd ComputerVisionProject
```
### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```
### **3. Set Up Environment Variables**
Create a ```.env``` file in the root directory and add your Azure credentials:

```env
ENDPOINT=https://your-endpoint.cognitiveservices.azure.com/
SUBSCRIPTION_KEY=your_subscription_key
```

### **4. Prepare Your Input**
Edit the ```image.json``` file to include the image URLs or local paths you want to analyze:

```json
{
  "images": [
    "https://example.com/image1.jpg",
    "https://example.com/image2.png"
  ]
}
```
### **5. Run the Script**
```bash
python vision_test.py
```

The script will analyze the images and display results such as:

- Image descriptions
- Tags and labels
- Objects detected
- Faces detected
- Color schemes and dominant colors
- Text extraction (OCR)

## 🧪 Requirements
The project uses the following Python packages:
```ini
azure-cognitiveservices-vision-computervision==0.7.0  
msrest==0.6.21  
requests==2.31.0  
python-dotenv==1.0.0  # Optional: Only needed if using a .env file for credentials
```

To install them manually:
```bash
pip install azure-cognitiveservices-vision-computervision msrest requests
```

If you're using a .env file to manage your API keys or environment variables, include:

```bash
pip install python-dotenv
```


## 📜 License
This project is licensed under the MIT License.
See the LICENSE file for more details.

## 🎓 Certificate
This project was completed as part of the Azure Computer Vision course on Coursera.
(https://coursera.org/share/0b8ae8ed5063bfe20c416931cd33ebed)

## 🙌 Acknowledgments
Special thanks to:
- Microsoft Azure — for providing the Computer Vision API.
- Coursera — for offering a structured learning platform.
- OpenAI — for assisting in technical documentation.

## ✨ Author
N. S. Dilara Liyanage
BSc (Hons.) in Computer Science — SLIIT
Passionate about ethical AI, ML, Data Science and sharing technical knowledge.

## 🔗 Connect with me:

- LinkedIn: https://www.linkedin.com/in/dilara-liyanage/
