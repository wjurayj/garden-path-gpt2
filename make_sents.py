import pandas as pd
import sys
import random

def get_components_npz(filename='npz', sent_type='gp', context=False, extension=False, comma=False):
    df = pd.read_csv(filename+'.tsv', sep='\t')
    cols = df.columns


    cols_ref = ['Start', 'Context', 'Intransitive Verb', 'Transitive Verb', 'Blocker',
    'Comma', 'NP/Z', 'Extension', 'Verb', 'Rest']
    trigger = 8
    # context & extension can be added to any index with no effect
    # comma can be added to negate GP effect

    idc = {'gp':[0, 3, 6, 8, 9], 'intransitive':[0, 2, 6, 8, 9], 'blocked':[0, 3, 4, 6, 8, 9]}
    idx = idc[sent_type]
    # idx = [0, 3, 5, 6, 8, 9] #basic comma

    if context:
        idx.append(1)
    if comma:
        idx.append(5)
    if extension:
        idx.append(7)

    idx.sort()

    tgt_cols = [cols[i] for i in idx]
    print('including columns:', tgt_cols)
    post = []
    pre = []
    # with open(filename+'.txt', 'w') as f:
    for i in range(len(df)):
        s = ''
        row = df.iloc[i]
        for j in idx:
            if j == trigger:
                pre.append(' '.join(s.split()))
                s = ''
            if j == 5:  #special case comma to attach to previous word
                s = s + str(row[cols[j]])
            else:
                s = s + ' ' + str(row[cols[j]])
        s = ' '.join(s.split())
        s = ' {}.\n'.format(s)
        post.append(s)
            # f.write(s)
    return pre, post

def make_sents_npz(filename='npz', sent_type='gp', context=False, extension=False, comma=False):
    pre, post = get_components_npz(filename=filename, sent_type=sent_type, context=context, extension=extension, comma=comma)
    return [pre[i] + ' ' + post[i] for i in range(len(post))]


def get_components_nps(filename='nps', sent_type='gp', context=False, extension=False, that=False):
    df = pd.read_csv(filename+'.tsv', sep='\t')
    cols = df.columns

    cols_ref = ['Subject', 'Context', 'Ambiguous Verb', 'Unambiguous Verb', 'That',
    'NP/S', 'Extension', 'Disambiguator', 'Rest']
    # context & extension can be added to any index with no effect
    # comma can be added to negate GP effect
    trigger = 7

    idc = {'gp':[0, 2, 5, 7, 8], 'unambiguous':[0, 3, 5, 7, 8]}
    idx = idc[sent_type]
    # idx = [0, 3, 5, 6, 8, 9] #basic comma

    if context:
        idx.append(1)
    if that:
        idx.append(4)
    if extension:
        idx.append(6)

    idx.sort()

    tgt_cols = [cols[i] for i in idx]
    print('including columns:', tgt_cols)
    pre = []
    post = []
    # with open(filename+'.txt', 'w') as f:
    for i in range(len(df)):
        s = ''
        row = df.iloc[i]
        for j in idx:
            if j == trigger:
                pre.append(' '.join(s.split()))
                s = ''
            s = s + ' ' + str(row[cols[j]])
        s = ' '.join(s.split())
        s = ' {}.\n'.format(s)
        post.append(s)
            # f.write(s)
    return pre, post

def make_sents_nps(filename='nps', sent_type='gp', context=False, extension=False, that=False):
    pre, post = get_components_nps(filename=filename, sent_type=sent_type, context=context, extension=extension, that=that)
    return [pre[i] + ' ' + post[i] for i in range(len(post))]

def get_components_va(filename='vawip', sent_type='gp', unreduced=False, intervener=False):
    df = pd.read_csv(filename+'.tsv', sep='\t')
    cols = df.columns

    cols_ref = ['Start', 'Noun', 'Unreduced Content' 'Ambiguous Verb', 'Unambiguous Verb', 'RC contents',
    'Intervener', 'Disambiguator', 'End']
    # context & extension can be added to any index with no effect
    # comma can be added to negate GP effect
    trigger = 7

    idc = {'gp':[0, 1, 3, 5, 7, 8], 'unambiguous':[0, 1, 4, 5, 7, 8]}
    idx = idc[sent_type]
    # idx = [0, 3, 5, 6, 8, 9] #basic comma

    if unreduced:
        idx.append(2)
    if intervener:
        idx.append(6)

    idx.sort()

    tgt_cols = [cols[i] for i in idx]
    print('including columns:', tgt_cols)
    pre = []
    post = []
    # with open(filename+'.txt', 'w') as f:
    for i in range(len(df)):
        s = ''
        row = df.iloc[i]
        for j in idx:
            if j == trigger:
                pre.append(' '.join(s.split()))
                s = ''
            s = s + ' ' + str(row[cols[j]])
        s = ' '.join(s.split())
        s = ' {}.\n'.format(s)
        post.append(s)
            # f.write(s)
    return pre, post

def make_sents_va(filename='vawip', sent_type='gp', unreduced=False, intervener=False):
    pre, post = get_components_va(filename=filename, sent_type=sent_type, unreduced=unreduced, intervener=intervener)
    return [pre[i] + ' ' + post[i] for i in range(len(post))]

def get_components_na(filename='nawip', sent_type='gp', that=False, extension=False):
    df = pd.read_csv(filename+'.tsv', sep='\t')
    cols = df.columns

    cols_ref = ['The', 'Ambiguous', 'Unambiguous' 'That', 'Subject', 'Extension',
    'Continuation', 'Disambiguator', 'Rest']
    # context & extension can be added to any index with no effect
    # comma can be added to negate GP effect
    trigger = 7

    idc = {'gp':[0, 1, 4, 6, 7, 8], 'unambiguous':[0, 2, 4, 6, 7, 8]}
    idx = idc[sent_type]
    # idx = [0, 3, 5, 6, 8, 9] #basic comma

    if that:
        idx.append(3)
    if extension:
        idx.append(5)

    idx.sort()

    tgt_cols = [cols[i] for i in idx]
    print('including columns:', tgt_cols)
    sents = []
    pre = []
    post = []
    # with open(filename+'.txt', 'w') as f:
    for i in range(len(df)):
        s = ''
        row = df.iloc[i]
        for j in idx:
            if j == trigger:
                pre.append(' '.join(s.split()))
                s = ''
            s = s + ' ' + str(row[cols[j]])
        s = ' '.join(s.split())
        s = ' {}.\n'.format(s)
        post.append(s)
            # f.write(s)
    return pre, post

def make_sents_na(filename='nawip', sent_type='gp', that=False, extension=False):
    pre, post = get_components_na(filename=filename, sent_type=sent_type, that=that, extension=extension)
    return [pre[i] + ' ' + post[i] for i in range(len(post))]

def write_sents(sents, filename='npz'):
    with open(filename+'.txt', 'w') as f:
        for s in sents:
            f.write(s)
    return