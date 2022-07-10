rs.compute # 比较两个化学反应相似度

function (rxnA, rxnB, format = "rsmi", standardize = T, 
    explicitH = F, reversible = T, algo = "msim", sim.method = "tanimoto", 
    fp.type = "extended", fp.mode = "bit", fp.depth = 6, 
    fp.size = 1024, verbose = F, fpCached = F) 
{
    format <- tolower(format)
    algo <- tolower(algo)
    sim.method[[1]] <- tolower(sim.method[[1]])
    fp.type <- tolower(fp.type)
    fp.mode <- tolower(fp.mode)
    if (missing(rxnA) || missing(rxnB)) {
        stop("Two reactions needed to compute similarity", 
            call. = F)
    }
    else if (length(rxnA) > 1 || length(rxnB) > 1) {
        warning("Input(s) has length > 1 and only the first element(s) will be used.")
        rxnA <- rxnA[[1]]
        rxnB <- rxnB[[1]]
    }
    if (!is.character(rxnA) || !is.character(rxnB)) {
        stop("Invalid input. Enter in (REACTION) SMILES format or path to RXN file.", 
            call. = F)
    }
    .algoCheck(algo)
    .fpTypeCheck(fp.type, fp.mode)
    .simTypeCheck(sim.method, fp.mode)
    if (length(format) == 1) {
        format[[2]] <- format[[1]]
    }
    result <- tryCatch({
        if (format[[1]] == "rsmi") {
            rA <- .rsmiParser(rxnA, standardize, explicitH)
        }
        else if (format[[1]] == "rxn") {
            rA <- .mdlParser(rxnA, standardize, explicitH)
        }
        else {
            stop("Invalid input format.", call. = F)
        }
        if (format[[2]] == "rsmi") {
            rB <- .rsmiParser(rxnB, standardize, explicitH)
        }
        else if (format[[2]] == "rxn") {
            rB <- .mdlParser(rxnB, standardize, explicitH)
        }
        else {
            stop("Invalid input format.", call. = F)
        }
        .similarity(rA, rB, reversible = reversible, algo = algo, 
            sim.method = sim.method, fp.type = fp.type, fp.mode = fp.mode, 
            fp.depth = fp.depth, fp.size = fp.size, verbose = verbose, 
            cached = fpCached)
    }, error = function(err) {
        stop(err)
    })
    result
}