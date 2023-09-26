from bs4 import BeautifulSoup
from urllib.request import urlopen
from pprint import pprint
from googletrans import Translator  #  pip3 install googletrans==3.1.0a0
import os
import markdownify
import requests

# cuidado ao usar o translate, pois pode ter correções manuais direto nos arquivos
def main(translate=False):
    
    baseurl = "https://docs.erpnext.com/docs/v14/user/manual/en"
    filesurl = "https://docs.erpnext.com"
    basepath = "./docs"
    translator = Translator()
    
    for page in pages():
        
        path = "/".join(page.split("/")[:-1]) # o último é o arquivo, então remove do path
        if not os.path.exists(basepath + "/en" + path):
            os.makedirs(basepath + "/en" + path)
        if not os.path.exists(basepath + "/pt" + path):
            os.makedirs(basepath + "/pt" + path)
                        
        url = baseurl + page
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")

        md = soup.find('div',{'class':'from-markdown'}) # obtem a tag com o conteudo markdown
        title = md.find('div',{'class':'align-items-center'}).contents[1] # obtem o titulo do texto que está em um div
        md.find('div',{'class':'align-items-center'}).replace_with(title) # substitui o div pelo seu conteudo
        
        # busca e download das imagens 
        for img in md.findAll('img'):
            imgname = img['src'].split("/")[-1] # obtem o nome do arquivo
            if imgname and not os.path.exists("./files/" + imgname):
                try:
                    img_data = requests.get(filesurl + img['src']).content
                except:
                    print(img['src'] + ' falhou no download')
                else:
                    img['src'] = "/files/" + imgname # troca o local da imagem
                    with open("./files/" + imgname, 'wb') as handler:
                        handler.write(img_data)
                    
        content_en = md.decode_contents()
        content_en = markdownify.markdownify(content_en, heading_style="ATX") # converte html para markdown        
        content_en = content_en.replace("/docs/v13/user/manual/en/", "/docs/en/") # substitui os links da documentação original
        content_en = content_en.replace("/docs/v14/user/manual/en/", "/docs/en/") # substitui os links da documentação original
        content_en = content_en.replace("/docs/v13/user/videos/", "https://docs.erpnext.com/docs/v13/user/videos/")
        content_en = content_en.replace("/docs/v14/user/videos/", "https://docs.erpnext.com/docs/v14/user/videos/")
        content_en = content_en.replace("ERPNext", "SOMA")
        content_en = content_en.replace("ERPnext", "SOMA")
        content_en = content_en.replace("{{", "&lcub;&lcub;") # substitui as chaves pois senão dá erro no markdown quando instalado no frappe
        
        fname = basepath + "/en" + page + ".md"
        f = open(fname, "w")
        f.write(content_en)
        f.close()
        
        if translate:
            content_pt = md.decode_contents()
            content_pt = translator.translate(content_pt, src='en', dest='pt').text # traduz para portugues
            content_pt = markdownify.markdownify(content_pt, heading_style="ATX") # converte html para markdown        
            content_pt = content_pt.replace("/docs/v13/user/manual/en/", "/docs/pt/") # substitui os links da documentação original
            content_pt = content_pt.replace("/docs/v14/user/manual/en/", "/docs/pt/") # substitui os links da documentação original
            content_pt = content_pt.replace("/docs/v13/user/videos/", "https://docs.erpnext.com/docs/v13/user/videos/")
            content_pt = content_pt.replace("/docs/v14/user/videos/", "https://docs.erpnext.com/docs/v14/user/videos/")
            content_pt = content_pt.replace("ERPNext", "SOMA")
            content_pt = content_pt.replace("ERPnext", "SOMA")
            content_pt = content_pt.replace("{{", "&lcub;&lcub;") # substitui as chaves pois senão dá erro no markdown quando instalado no frappe

            fname = basepath + "/pt" + page + ".md"
            f = open(fname, "w")
            f.write(content_pt)
            f.close()



def pages():
    return [
    "/accounts",
    "/accounts/accounting-dimension-filter",
    "/accounts/accounting-dimensions",
    "/accounts/accounting-entries",
    "/accounts/accounting-period",
    "/accounts/accounting-reports",
    "/accounts/accounts-settings",
    "/accounts/advance-payment-entry",
    "/accounts/articles/accounting-for-bad-debts",
    "/accounts/articles/adding-reference-to-journal-entry",
    "/accounts/articles/additional-charges-in-payment",
    "/accounts/articles/adjusting-withhold-amount",
    "/accounts/articles/allocating-credit-note-and-payment",
    "/accounts/articles/balance-in-temporary-account",
    "/accounts/articles/book-discount-allowed-and-received-separately",
    "/accounts/articles/bulk-payment-entry",
    "/accounts/articles/changing-parent-account",
    "/accounts/articles/common_party_accounting",
    "/accounts/articles/common-receivable-account",
    "/accounts/articles/customise-cash-flow-report",
    "/accounts/articles/debit-note-for-price-adjustment",
    "/accounts/articles/default-receivable-payable-account",
    "/accounts/articles/delete-entries-linked-with-gl-entries",
    "/accounts/articles/difference-entry-button",
    "/accounts/articles/difference-in-total-and-valuation-in-tax-and-charges",
    "/accounts/articles/discount_accounting",
    "/accounts/articles/exchange-rate-field-frozen",
    "/accounts/articles/fiscal-year-creation",
    "/accounts/articles/fiscal-year-error",
    "/accounts/articles/freeze-account",
    "/accounts/articles/freeze-accounting-entries",
    "/accounts/articles/gst-for-multiple-branches",
    "/accounts/articles/how-to-apply-tax-on-tax",
    "/accounts/articles/immutable-ledger-in-erpnext",
    "/accounts/articles/invoice-rounding-issue",
    "/accounts/articles/landed-cost-voucher",
    "/accounts/articles/manage-foreign-exchange-difference",
    "/accounts/articles/managing-invoice-discount-in-the-payment-entry",
    "/accounts/articles/merging-accounts",
    "/accounts/articles/mode_of_payment",
    "/accounts/articles/naming-series-as-per-gst-rules",
    "/accounts/articles/opening-invoice-creation-tool",
    "/accounts/articles/payment_ledger",
    "/accounts/articles/payment-entry-for-capital-account",
    "/accounts/articles/perpetual-inventory-for-non-stock-item",
    "/accounts/articles/petty-cash-entry-in-erpnext",
    "/accounts/articles/post-dated-cheque-entry",
    "/accounts/articles/print-cancelled-invoice",
    "/accounts/articles/purchase-invoice-account-type-error",
    "/accounts/articles/reconcile-advance-payment-made-to-the-supplier",
    "/accounts/articles/round-off-account-validation",
    "/accounts/articles/stock-transfer-with-gst",
    "/accounts/articles/tax-inclusive-accounting",
    "/accounts/articles/tax-on-another-tax-amount",
    "/accounts/articles/types-in-tax-template",
    "/accounts/articles/update-gstr-1-data-in-gst-offline-tool",
    "/accounts/articles/warehouse-ledger-link",
    "/accounts/articles/withdrawing-salary-from-owners-equity-account",
    "/accounts/bank",
    "/accounts/bank-account",
    "/accounts/bank-guarantee",
    "/accounts/bank-reconciliation",
    "/accounts/budgeting",
    "/accounts/chart-of-accounts",
    "/accounts/cost-center",
    "/accounts/credit-limit",
    "/accounts/credit-note",
    "/accounts/currency",
    "/accounts/currency-exchange",
    "/accounts/debit-note",
    "/accounts/deferred_revenue/expense_report",
    "/accounts/deferred-expense",
    "/accounts/deferred-revenue",
    "/accounts/distributed-cost-center",
    "/accounts/dunning",
    "/accounts/exchange-rate-revaluation",
    "/accounts/finance-book",
    "/accounts/fiscal-year",
    "/accounts/inter-company-invoices",
    "/accounts/inter-company-journal-entry",
    "/accounts/invoice_discounting",
    "/accounts/item-tax-template",
    "/accounts/journal-entry",
    "/accounts/journal-entry-template",
    "/accounts/loyalty-program",
    "/accounts/mode-of-payment",
    "/accounts/multi-currency-accounting",
    "/accounts/opening-balance",
    "/accounts/payment_terms_status_report",
    "/accounts/payment-entry",
    "/accounts/payment-order",
    "/accounts/payment-reconciliation",
    "/accounts/payment-request",
    "/accounts/payment-terms",
    "/accounts/payment-terms-template",
    "/accounts/period-closing-voucher",
    "/accounts/point-of-sales",
    "/accounts/pos_invoice_consolidation",
    "/accounts/pos-profile",
    "/accounts/pricing-rule",
    "/accounts/process-deferred-accounting",
    "/accounts/process-statement-of-accounts",
    "/accounts/promotional-scheme",
    "/accounts/purchase-invoice",
    "/accounts/quickbooks-migrator",
    "/accounts/sales-invoice",
    "/accounts/semi-auto-payment-reconciliation",
    "/accounts/shareholder",
    "/accounts/share-reports",
    "/accounts/share-transfer",
    "/accounts/subscription",
    "/accounts/subscription-plan",
    "/accounts/subscription-settings",
    "/accounts/tax-category",
    "/accounts/tax-rule",
    "/accounts/tax-withholding-category",
    "/automation",
    "/automation/assignment-rule",
    "/automation/auto-repeat",
    "/automation/event_streaming",
    "/automation/milestone-tracker",
    "/CRM",
    "/CRM/address",
    "/CRM/appointment",
    "/CRM/appointment-booking-settings",
    "/CRM/articles/automate_lead_capturing",
    "/CRM/articles/difference_between_lead_contact_and_customer",
    "/CRM/articles/sales_funnel",
    "/CRM/campaign",
    "/CRM/contact",
    "/CRM/contract",
    "/CRM/crm_reports",
    "/CRM/crm_settings",
    "/CRM/customer",
    "/CRM/customer-group",
    "/CRM/email_group",
    "/CRM/email-campaign",
    "/CRM/lead",
    "/CRM/lead_source",
    "/CRM/linkedin-settings",
    "/CRM/newsletter",
    "/CRM/opportunity",
    "/CRM/opportunity_type",
    "/CRM/sales_stage",
    "/CRM/sales-person",
    "/CRM/social-media-post",
    "/CRM/twitter-settings",
    "/customize-erpnext",
    "/customize-erpnext/articles/add-remove-fields-from-print-format",
    "/customize-erpnext/articles/centavo-being-printed-in-words-for-usd",
    "/customize-erpnext/articles/change-custom-field-datatype-after-field-creation",
    "/customize-erpnext/articles/company-wise-naming-series",
    "/customize-erpnext/articles/creating-custom-link-field",
    "/customize-erpnext/articles/customise-your-items-tables-within-your-print-format-builder",
    "/customize-erpnext/articles/customizing-data-visibility-in-child-table",
    "/customize-erpnext/articles/customizing-sorting-order-in-the-list-view",
    "/customize-erpnext/articles/deleting-custom-reports",
    "/customize-erpnext/articles/disable-rounded-total",
    "/customize-erpnext/articles/document-title-with-multiple-fields",
    "/customize-erpnext/articles/dynamic-link-fields",
    "/customize-erpnext/articles/editing-a-field-after-submission",
    "/customize-erpnext/articles/electronic-signature",
    "/customize-erpnext/articles/export-data-for-specific-year-or-filter",
    "/customize-erpnext/articles/feedback-request-using-web-form",
    "/customize-erpnext/articles/fetch-child-table-values-using-jinja-tags",
    "/customize-erpnext/articles/fetching-data-from-a-document",
    "/customize-erpnext/articles/field-types",
    "/customize-erpnext/articles/geolocation-field",
    "/customize-erpnext/articles/how-to-add-columns-in-the-standard-report-and-export",
    "/customize-erpnext/articles/how-to-add-master-link-and-fetch-data-from-the-same",
    "/customize-erpnext/articles/making-custom-reports",
    "/customize-erpnext/articles/making-fields-visible-in-print-format",
    "/customize-erpnext/articles/maximum-number-of-fields-in-a-form",
    "/customize-erpnext/articles/removing-description-removed-item-code-and-name",
    "/customize-erpnext/articles/reports-showing-multiple-lines-for-one-document",
    "/customize-erpnext/articles/search-record-by-specific-field",
    "/customize-erpnext/articles/table-multiselect-field",
    "/customize-erpnext/authorization-rule",
    "/customize-erpnext/client-scripts",
    "/customize-erpnext/client-scripts/custom-button",
    "/customize-erpnext/client-scripts/date-validation",
    "/customize-erpnext/client-scripts/fetch%20value%20in%20child%20table%20field",
    "/customize-erpnext/client-scripts/fetch-values-from-master",
    "/customize-erpnext/client-scripts/filter-options-in-select-field",
    "/customize-erpnext/client-scripts/generate-item-code-based-on-custom-logic",
    "/customize-erpnext/client-scripts/hide-buttons-in-form-view",
    "/customize-erpnext/client-scripts/lock_timesheets_based_on_date",
    "/customize-erpnext/client-scripts/make-read-only-after-saving",
    "/customize-erpnext/client-scripts/rename-buttons-in-form-view",
    "/customize-erpnext/client-scripts/restrict-cancel-rights",
    "/customize-erpnext/client-scripts/restrict-purpose-of-stock-entry",
    "/customize-erpnext/client-scripts/restrict-user-based-on-child-record",
    "/customize-erpnext/client-scripts/sales-invoice-id-based-on-sales-order-id",
    "/customize-erpnext/client-scripts/update-date-field-based-on-value-in-other-date-field",
    "/customize-erpnext/custom-field",
    "/customize-erpnext/customize-form",
    "/customize-erpnext/customizing-module-visibility",
    "/customize-erpnext/desk-page",
    "/customize-erpnext/doctype",
    "/customize-erpnext/document-states",
    "/customize-erpnext/document-title",
    "/customize-erpnext/kanban-board",
    "/customize-erpnext/print-format",
    "/customize-erpnext/server-script",
    "/introduction",
    "/introduction/concepts-and-terms",
    "/introduction/do-i-need-an-erp",
    "/introduction/getting-started-with-erpnext",
    "/introduction/implementation-strategy",
    "/introduction/key-workflows",
    "/introduction/the-champion",
    "/setting-up",
    "/setting-up/articles/change-password",
    "/setting-up/articles/changing-the-properties-of-a-field-based-on-role",
    "/setting-up/articles/configuring-a-reply-to-email-address-in-erpnext",
    "/setting-up/articles/delete-submitted-document",
    "/setting-up/articles/difference-between-system-user-and-website-user",
    "/setting-up/articles/easy-steps-to-setup-workflow",
    "/setting-up/articles/edit-submitted-document",
    "/setting-up/articles/email-error",
    "/setting-up/articles/how-to-change-a-users-email-id",
    "/setting-up/articles/how-to-disable-notification-emails-for-energy-points",
    "/setting-up/articles/how-to-disable-users-in-the-erpnext-system",
    "/setting-up/articles/how-to-export-data-from-erpnext-to-excel-csv",
    "/setting-up/articles/how-to-fix-the-reached-maximum-user-limit-for-your-subscription-issue",
    "/setting-up/articles/how-to-grant-permissions-for-reports",
    "/setting-up/articles/importing-historical-data-in-a-doctype-with-workflow",
    "/setting-up/articles/include-document-link-in-notification-email",
    "/setting-up/articles/integrating-erpnext-with-biometric-attendance-devices",
    "/setting-up/articles/managing-perm-level",
    "/setting-up/articles/managing-tree-structure-masters",
    "/setting-up/articles/naming-series-current-value",
    "/setting-up/articles/perm-level-error-in-permission-manager",
    "/setting-up/articles/prepared-report",
    "/setting-up/articles/print-format-sections",
    "/setting-up/articles/remove-link-at-the-bottom-of-the-print-page",
    "/setting-up/articles/report-permission-error",
    "/setting-up/articles/set-language",
    "/setting-up/articles/set-precision",
    "/setting-up/articles/setting-default-values-for-any-field-in-erpnext",
    "/setting-up/articles/setting-up-email-signature-in-erpnext",
    "/setting-up/articles/setting-up-sendgrid-smtp-email-in-erpnext",
    "/setting-up/articles/setting-workflows-on-masters",
    "/setting-up/articles/setup-two-factor-authentication",
    "/setting-up/articles/user-restriction",
    "/setting-up/articles/using-custom-domain-on-erpnext",
    "/setting-up/articles/what-if-emails-are-not-being-received-by-the-recipients",
    "/setting-up/bulk-update",
    "/setting-up/chart-of-accounts-importer",
    "/setting-up/company-setup",
    "/setting-up/data",
    "/setting-up/data/data-export",
    "/setting-up/data/data-import",
    "/setting-up/data/download-backup",
    "/setting-up/domain-settings",
    "/setting-up/email",
    "/setting-up/email/auto-email-reports",
    "/setting-up/email/document-follow",
    "/setting-up/email/email-account",
    "/setting-up/email/email-digest",
    "/setting-up/email/email-domain",
    "/setting-up/email/email-dropbox",
    "/setting-up/email/email-inbox",
    "/setting-up/email/email-template",
    "/setting-up/email/linking-emails-to-document",
    "/setting-up/email/sending-email",
    "/setting-up/energy-point-system",
    "/setting-up/personal-data-deletion",
    "/setting-up/personal-data-download",
    "/setting-up/print",
    "/setting-up/print/address-template",
    "/setting-up/print/cheque-print-template",
    "/setting-up/print/custom-translations",
    "/setting-up/print/letter-head",
    "/setting-up/print/print-format",
    "/setting-up/print/print-format-builder",
    "/setting-up/print/print-headings",
    "/setting-up/print/print-settings",
    "/setting-up/print/print-style",
    "/setting-up/print/raw-printing",
    "/setting-up/print/terms-and-conditions",
    "/setting-up/setting-company-sales-goal",
    "/setting-up/settings",
    "/setting-up/settings/bulk-rename",
    "/setting-up/settings/document-naming-settings",
    "/setting-up/settings/global-defaults",
    "/setting-up/settings/session-defaults",
    "/setting-up/settings/show-hide-modules",
    "/setting-up/settings/system-settings",
    "/setting-up/setting-up-taxes",
    "/setting-up/sms-setting",
    "/setting-up/users-and-permissions",
    "/setting-up/users-and-permissions/adding-users",
    "/setting-up/users-and-permissions/administrator",
    "/setting-up/users-and-permissions/limited-user",
    "/setting-up/users-and-permissions/role-and-role-profile",
    "/setting-up/users-and-permissions/role-based-permissions",
    "/setting-up/users-and-permissions/role-permission-for-page-and-report",
    "/setting-up/users-and-permissions/sharing",
    "/setting-up/users-and-permissions/user-permissions",
    "/setting-up/workflow-actions",
    "/setting-up/workflows",
    "/setting-up/workflow-state",
    "/support",
    "/support/articles/automating-issue-assignments-to-support-team-in-erpnext",
    "/support/issue",
    "/support/issue-type-and-priority",
    "/support/maintenance-schedule",
    "/support/maintenance-visit",
    "/support/service-level-agreement",
    "/support/support_reports",
    "/support/support-settings",
    "/support/warranty-claim",
    "/using-erpnext",
    "/using-erpnext/access-log",
    "/using-erpnext/articles/adding-attachments-to-outgoing-messages",
    "/using-erpnext/articles/bulk-rename",
    "/using-erpnext/articles/check-link-between-documents",
    "/using-erpnext/articles/copy-pasting-multiple-records-from-excel",
    "/using-erpnext/articles/duplicate-record",
    "/using-erpnext/articles/how-to-restore-deleted-documents-in-erpnext",
    "/using-erpnext/articles/how-to-sync-doc-types-with-calendar",
    "/using-erpnext/articles/letter-head-in-the-report",
    "/using-erpnext/articles/renaming-documents",
    "/using-erpnext/articles/todo-auto-creation",
    "/using-erpnext/articles/tree-master-renaming",
    "/using-erpnext/assignment",
    "/using-erpnext/calendar",
    "/using-erpnext/collaborating-around-forms",
    "/using-erpnext/dashboard",
    "/using-erpnext/desktop",
    "/using-erpnext/document-versioning",
    "/using-erpnext/filter-by",
    "/using-erpnext/Global-search",
    "/using-erpnext/notes",
    "/using-erpnext/restore-deleted-docs",
    "/using-erpnext/save-filter",
    "/using-erpnext/search-filter",
    "/using-erpnext/tags",
    "/using-erpnext/to-do",
    "/using-erpnext/video"
    ]
    
main(True) # cuidado ao usar o translate, pois pode ter correções manuais direto nos arquivos