from __future__ import absolute_import

from collections import OrderedDict

from pythesint.json_vocabulary import JSONVocabulary, openURL


class GCMDVocabulary(JSONVocabulary):
    def _fetch_online_data(self):
        ''' Return list of GCMD standard keywords at provided url

        Parameters
        ----------
        list_name : the GCMD list name (must be one of the items in the standard_lists
        dictionary) in which;
            url is the URL of the desired GCMD list of valid keywords
            keyword_groups is a list containing the grouping of the keywords, e.g.,
            ['Category', 'Short_Name', 'Long_Name'] - used for verification
        '''
        response = openURL(self.url)
        # Boolean to determine if line information in the response object should be
        # stored as keywords
        do_record = False

        gcmd_list = []
        kw_groups = []
        for line in response.readlines():
            read_line(line, gcmd_list, do_record, kw_groups)

        return gcmd_list


def read_line(line, gcmd_list, do_record, kw_groups):
    if 'Keyword Version' and 'Revision' in line:
        meta = line.split('","')
        gcmd_list.append({'Revision': meta[1][10:]})
    if do_record:
        gcmd_keywords = line.split('","')
        gcmd_keywords[0] = gcmd_keywords[0].strip('"')
        if gcmd_keywords[0] == 'NOT APPLICABLE':
            continue
        # Remove last item (the ID is not needed)
        gcmd_keywords.pop(-1)
        if len(gcmd_keywords) != len(kw_groups):
            continue
        line_kw = OrderedDict()
        for i, key in enumerate(kw_groups):
            line_kw[key] = gcmd_keywords[i]
        gcmd_list.append(line_kw)
    if line.split(',')[0].lower() == self.categories[0].lower():
        do_record = True
        kw_groups = line.split(',')
        kw_groups.pop(-1)
        # Make sure the group items are as expected
        if kw_groups != self.categories:
            raise TypeError('%s is not equal to %s' %
                            (kw_groups, self.categories))