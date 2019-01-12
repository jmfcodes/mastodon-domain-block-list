# assuming there are NO headers when copying and pasting from https://exampleinstance.com/admin/domain_blocks
with open('domainblocks.txt', 'r') as domain_file:
    lines = domain_file.readlines()
    domains = []
    for line in lines:
        domain = line.split('\t')
        domains.append({ 'domain': domain[0], 'severity': domain[1] })

# alphabetize the list for readability
sorted_domains = sorted(domains, key=lambda k: k['domain'])

# create a list where each item is HTML for one row of the table
header = ['Domain', 'Severity']
html_rows = ['<table class="domain-block-list"><tbody>\n<tr><td>' + header[0] + '</td><td>' + header[1] + '</td></tr>\n']
for domain in sorted_domains:
    html_rows.append('<tr class="domain"><td>' + domain['domain'] + '</td><td>' + domain['severity'] + '</td></tr>\n')
html_rows.append('</tbody></table>\n')

# now add a little CSS for readability
css = '''
<style type="text/css">
.domain-block-list {
  border-collapse: collapse;
  }

.domain-block-list td {
  border: solid black 1px;
  padding: 10px 5px;
  }

.domain-block-list tr:first-child {
  font-weight: bold;
  text-transform: uppercase;
}

</style>
'''

# finally: generate a file for pasting into https://exampleinstance.com/admin/settings/edit
with open('domain_block_list.html', 'w') as html_for_pasting:
    html_for_pasting.write(css)
    for row in html_rows:
        html_for_pasting.write(row)
