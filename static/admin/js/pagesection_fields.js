/* Page-builder admin UX: show only the fields relevant to the selected section
 * "Kind". Runs for every PageSection inline form, on load, on change, and when
 * a new inline row is added. `kind`, `background` and `is_published` always show.
 */
(function () {
  "use strict";

  // Which toggleable fields are relevant for each section kind.
  var MAP = {
    text:       ["eyebrow", "heading", "body", "image"],
    treatments: ["eyebrow", "heading"],
    counters:   ["eyebrow", "heading", "items"],
    why:        ["eyebrow", "heading", "body", "items"],
    faq:        [],
    reviews:    [],
    brands:     ["eyebrow", "heading"],
    cta:        ["heading", "body", "button_text", "button_url"]
  };
  // All fields that can be shown/hidden (everything else is always visible).
  var TOGGLE = ["eyebrow", "heading", "body", "items", "image", "button_text", "button_url"];

  function applyForm(form) {
    var sel = form.querySelector('select[name$="-kind"]');
    if (!sel) return;
    var show = MAP[sel.value] || TOGGLE;
    TOGGLE.forEach(function (name) {
      var row = form.querySelector(".form-row.field-" + name) || form.querySelector(".field-" + name);
      if (row) row.style.display = show.indexOf(name) !== -1 ? "" : "none";
    });
  }

  function init() {
    var forms = document.querySelectorAll(".inline-related");
    Array.prototype.forEach.call(forms, function (form) {
      var sel = form.querySelector('select[name$="-kind"]');
      if (!sel || sel.dataset.psBound) return;
      sel.dataset.psBound = "1";
      applyForm(form);
      sel.addEventListener("change", function () { applyForm(form); });
    });
  }

  document.addEventListener("DOMContentLoaded", init);
  // New inline rows added via "Add another" (Django 5 dispatches a native event;
  // older versions dispatch a jQuery event).
  document.addEventListener("formset:added", init);
  if (window.django && window.django.jQuery) {
    window.django.jQuery(document).on("formset:added", init);
  }
})();
