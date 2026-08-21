import nodemailer from "nodemailer";

const TO = process.env.QUOTE_TO || "thistleflooringinstalls@gmail.com";
const FROM_USER = process.env.GMAIL_USER || "thistleflooringinstalls@gmail.com";
const PASS = process.env.GMAIL_APP_PASSWORD || "";

let transporter;

function getTransporter() {
  if (!PASS) return null;
  if (!transporter) {
    transporter = nodemailer.createTransport({
      service: "gmail",
      auth: { user: FROM_USER, pass: PASS },
    });
  }
  return transporter;
}

export function mailConfigured() {
  return Boolean(PASS);
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function row(label, value) {
  if (!value) return "";
  return `<tr>
    <td style="padding:8px 12px 8px 0;color:#6d665d;vertical-align:top;white-space:nowrap;">${escapeHtml(label)}</td>
    <td style="padding:8px 0;color:#1a1816;">${escapeHtml(value).replace(/\n/g, "<br>")}</td>
  </tr>`;
}

export async function sendQuote({ name, email, phone, project, sqft, message }) {
  const transport = getTransporter();
  if (!transport) {
    const err = new Error("Email is not configured");
    err.code = "NOT_CONFIGURED";
    throw err;
  }

  const subject = `Quote request — ${project || "Flooring"} — ${name}`;
  const text = [
    "New quote request from thistleflooring.ca",
    "",
    `Name: ${name}`,
    `Email: ${email}`,
    phone ? `Phone: ${phone}` : null,
    project ? `Project: ${project}` : null,
    sqft ? `Approximate sq ft: ${sqft}` : null,
    "",
    message || "(No additional details)",
  ]
    .filter((line) => line !== null)
    .join("\n");

  const html = `
    <div style="font-family:Georgia,serif;max-width:560px;color:#1a1816;">
      <p style="font-size:12px;letter-spacing:0.18em;text-transform:uppercase;color:#c4a35a;margin:0 0 8px;">Thistle Flooring</p>
      <h1 style="font-size:22px;font-weight:500;margin:0 0 16px;">New quote request</h1>
      <table style="font-size:15px;line-height:1.5;border-collapse:collapse;">
        ${row("Name", name)}
        ${row("Email", email)}
        ${row("Phone", phone)}
        ${row("Project", project)}
        ${row("Sq ft", sqft)}
        ${row("Details", message)}
      </table>
      <p style="margin-top:24px;font-size:13px;color:#6d665d;">Reply to this email to write ${escapeHtml(name)} directly.</p>
    </div>
  `;

  await transport.sendMail({
    from: `Thistle Flooring Website <${FROM_USER}>`,
    to: TO,
    replyTo: `${name} <${email}>`,
    subject,
    text,
    html,
  });
}
