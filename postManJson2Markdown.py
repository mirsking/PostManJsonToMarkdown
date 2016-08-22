import json
import sys

def print_help(cmd):
    print "Usage: %s json_file markdown_file" % cmd

if __name__=='__main__':
    if len(sys.argv)!=3:
        print_help(sys.argv[0])

    json_filename = sys.argv[1]
    markdown_filename = sys.argv[2]

    with open(json_filename, 'r') as jfile:
        contents = json.load(jfile)
        with open(markdown_filename, 'w') as mfile:
            sys.stdout = mfile

            print "## " + contents['info']['name']
            items = contents['item']
            for item in items:
                print "### " + item['name']
                print "#### Request"
                req = item['request']
                ## print description
                description = req['description']
                print description

                print "```javascript"
                print req['method'] + " " + req['url']

                ## print header
                header = req['header']
                if len(header) != 0:
                    print 'header:'
                    count = 0
                    print "{"
                    for keyVal in header:
                        str = "\t" + keyVal['key'] + ": " + keyVal['value']
                        count += 1
                        if count < len(header):
                            print str+","
                        else:
                            print str
                    print "}"

                ## print body
                body = req['body']
                if body['mode'] == 'raw':
                    print 'body:'
                    print body['raw']

                print "```"

                # print "#### Response Payload"
                # res = item['response']
                # print "```"
                # print res
                # print "```"