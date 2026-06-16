import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Jewelry Tool", page_icon="💍", layout="centered")

components.html("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <style>
    *, *::before, *::after { box-sizing: border-box; }

    body {
      margin: 0;
      padding: 1.5rem 1rem 2rem;
      background-color: transparent;
      color: #FAFAFA;
      font-family: "Source Sans Pro", sans-serif;
      font-size: 16px;
    }

    h2 {
      font-size: 1.4rem;
      font-weight: 600;
      color: #FAFAFA;
      margin: 0 0 0.25rem;
    }

    p.subtitle {
      color: #A0A4B0;
      font-size: 0.95rem;
      margin: 0 0 1.5rem;
    }

    fieldset {
      border: 1px solid #3D3D3D;
      border-radius: 8px;
      padding: 1rem 1.25rem;
      margin-bottom: 1rem;
      background: #1E1E1E;
    }

    legend {
      font-weight: 600;
      font-size: 0.9rem;
      color: #FAFAFA;
      padding: 0 0.4rem;
    }

    label {
      display: block;
      font-size: 0.9rem;
      color: #FAFAFA;
      margin-bottom: 0.75rem;
    }

    label span {
      display: block;
      margin-bottom: 0.3rem;
      font-weight: 600;
      font-size: 0.85rem;
      color: #A0A4B0;
      text-transform: uppercase;
      letter-spacing: 0.03em;
    }

    select, textarea, input[type="text"] {
      width: 100%;
      padding: 0.45rem 0.65rem;
      border: 1px solid #3D3D3D;
      border-radius: 6px;
      font-family: inherit;
      font-size: 0.95rem;
      color: #FAFAFA;
      background: #262730;
      outline: none;
      transition: border-color 0.15s;
      resize: vertical;
    }

    select:focus, textarea:focus {
      border-color: #FF4B4B;
      box-shadow: 0 0 0 2px rgba(255,75,75,0.15);
    }

    .gem-grid, .watch-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.5rem 1rem;
    }

    .hidden { display: none; }

    .btn-row {
      display: flex;
      gap: 0.75rem;
      margin-top: 0.75rem;
    }

    button {
      flex: 1;
      padding: 0.55rem 1rem;
      border: none;
      border-radius: 6px;
      font-family: inherit;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      transition: opacity 0.15s;
    }

    button:hover { opacity: 0.85; }

    #generateBtn {
      background-color: #FF4B4B;
      color: #FFFFFF;
    }

    #copyBtn {
      background-color: #262730;
      color: #FAFAFA;
      border: 1px solid #3D3D3D;
    }

    #output {
      min-height: 4rem;
      background: #262730;
      font-size: 0.9rem;
    }

    .copy-feedback {
      font-size: 0.8rem;
      color: #21A453;
      margin-top: 0.3rem;
      min-height: 1.1rem;
    }
  </style>
</head>
<body>

  <h2>💍 Scheduled Item Tool</h2>
  <p class="subtitle">Collect information on the item being scheduled.</p>

  <fieldset>
    <legend>Item Type</legend>
    <label>
      <span>Item Type</span>
      <select id="itemTypes" onchange="watchSelected()">
        <option value="Ring">Ring</option>
        <option value="Necklace">Necklace</option>
        <option value="Bracelet">Bracelet</option>
        <option value="Watch">Watch</option>
        <option value="Earrings">Earrings</option>
        <option value="Other" selected>Other</option>
      </select>
    </label>
  </fieldset>

  <fieldset>
    <legend>Gemstone Details</legend>
    <label>
      <span>Does item have gemstones?</span>
      <select id="hasGems" onchange="gemSelect()">
        <option value="yes">Yes</option>
        <option value="no" selected>No</option>
      </select>
    </label>
    <fieldset id="additionalGemDetails" class="hidden">
      <legend>Gemstone Information</legend>
      <div class="gem-grid">
        <label><span>Type</span><textarea id="gemType" rows="1" placeholder="e.g. Diamond"></textarea></label>
        <label><span>Cut</span><textarea id="gemCut" rows="1" placeholder="e.g. Round"></textarea></label>
        <label><span>Color</span><textarea id="gemColor" rows="1" placeholder="e.g. D"></textarea></label>
        <label><span>Clarity</span><textarea id="gemClarity" rows="1" placeholder="e.g. VS1"></textarea></label>
        <label><span>Carats</span><textarea id="gemCarats" rows="1" placeholder="e.g. 1.5"></textarea></label>
        <label><span>Weight</span><textarea id="gemWeight" rows="1" placeholder="e.g. 2.3g"></textarea></label>
      </div>
    </fieldset>
  </fieldset>

  <fieldset id="additionalWatchDetails" class="hidden">
    <legend>Watch Information</legend>
    <div class="watch-grid">
      <label><span>Model #</span><textarea id="watchModel" rows="1" placeholder="e.g. 116610LN"></textarea></label>
      <label><span>Name</span><textarea id="watchName" rows="1" placeholder="e.g. Submariner"></textarea></label>
      <label><span>Color</span><textarea id="watchColor" rows="1" placeholder="e.g. Black dial"></textarea></label>
    </div>
  </fieldset>

  <fieldset>
    <legend>Other Information</legend>
    <div class="gem-grid">
      <label><span>Markings</span><textarea id="otherMarkings" rows="1" placeholder="e.g. 14K, 585"></textarea></label>
      <label><span>Metal Type</span><textarea id="otherMetalType" rows="1" placeholder="e.g. Yellow Gold"></textarea></label>
      <label><span>Appraisal Date</span><textarea id="otherAppraisalDate" rows="1" placeholder="e.g. 01/2024"></textarea></label>
      <label><span>Appraisal Price</span><textarea id="otherAppraisalPrice" rows="1" placeholder="e.g. 5000"></textarea></label>
    </div>
  </fieldset>

  <fieldset>
    <legend>Generated Description</legend>
    <label>
      <span>Copy into quoting system</span>
      <textarea id="output" rows="4" placeholder="Click Generate Description…" readonly></textarea>
    </label>
    <div class="btn-row">
      <button id="generateBtn" onclick="generateDescription()">Generate Description</button>
      <button id="copyBtn" onclick="copyDescriptionFunc()">Copy</button>
    </div>
    <div class="copy-feedback" id="copyFeedback"></div>
  </fieldset>

  <script>
    function gemSelect() {
      const val = document.getElementById("hasGems").value;
      document.getElementById("additionalGemDetails").classList.toggle("hidden", val !== "yes");
    }

    function watchSelected() {
      const val = document.getElementById("itemTypes").value;
      document.getElementById("additionalWatchDetails").classList.toggle("hidden", val !== "Watch");
    }

    function generateDescription() {
      const itemType = document.getElementById("itemTypes").value;
      const gemType = document.getElementById("gemType").value.trim();
      const gemCut = document.getElementById("gemCut").value.trim();
      const gemColor = document.getElementById("gemColor").value.trim();
      const gemClarity = document.getElementById("gemClarity").value.trim();
      const gemCarats = document.getElementById("gemCarats").value.trim();
      const gemWeight = document.getElementById("gemWeight").value.trim();
      const watchModel = document.getElementById("watchModel").value.trim();
      const watchName = document.getElementById("watchName").value.trim();
      const watchColor = document.getElementById("watchColor").value.trim();
      const otherMarkings = document.getElementById("otherMarkings").value.trim();
      const otherMetalType = document.getElementById("otherMetalType").value.trim();
      const otherAppraisalDate = document.getElementById("otherAppraisalDate").value.trim();
      const otherAppraisalPrice = document.getElementById("otherAppraisalPrice").value.trim();

      let description = `Item Type: ${itemType}`;

      if (gemType) {
        description += `; Gemstone: ${gemCarats ? gemCarats + "-carat " : ""}${gemType}`;
        const gemDetails = [];
        if (gemCut) gemDetails.push(`Cut: ${gemCut}`);
        if (gemColor) gemDetails.push(`Color: ${gemColor}`);
        if (gemClarity) gemDetails.push(`Clarity: ${gemClarity}`);
        if (gemWeight) gemDetails.push(`Weight: ${gemWeight}`);
        if (gemDetails.length) description += ` (${gemDetails.join(", ")})`;
      }

      const watchDetails = [];
      if (watchModel) watchDetails.push(`Model: ${watchModel}`);
      if (watchName) watchDetails.push(`Name: ${watchName}`);
      if (watchColor) watchDetails.push(`Color: ${watchColor}`);
      if (watchDetails.length) description += `; Watch Details: ${watchDetails.join(", ")}`;

      const otherDetails = [];
      if (otherMarkings) otherDetails.push(`Markings: ${otherMarkings}`);
      if (otherMetalType) otherDetails.push(`Metal: ${otherMetalType}`);
      if (otherAppraisalDate) otherDetails.push(`Appraisal Date: ${otherAppraisalDate}`);
      if (otherAppraisalPrice) {
        const price = Number(otherAppraisalPrice).toLocaleString("en-US", { style: "currency", currency: "USD" });
        otherDetails.push(`Appraisal Price: ${price}`);
      }
      if (otherDetails.length) description += `; ${otherDetails.join(", ")}`;

      document.getElementById("output").value = description;
    }

    function copyDescriptionFunc() {
      const output = document.getElementById("output");
      navigator.clipboard.writeText(output.value).then(() => {
        const fb = document.getElementById("copyFeedback");
        fb.textContent = "Copied to clipboard!";
        setTimeout(() => fb.textContent = "", 2000);
      });
    }

    gemSelect();
    watchSelected();
  </script>
</body>
</html>
""", height=900, scrolling=True)
